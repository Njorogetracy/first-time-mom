from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Activity(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    max_participants = models.PositiveIntegerField(default=10)
    is_cancelled = models.BooleanField(default=False)
    type_choices = [
        ('Class', 'Class'),
        ('Group Counseling', 'Group Counseling'),
        ('Yoga Session', 'Yoga Session'),
    ]
    type = models.CharField(
        max_length=20,
        choices=type_choices,
        default='Class',
        )

    def __str__(self):
        return f"{self.name} on {self.date}"

    def current_num_of_participants(self):
        num_bookings = Booking.objects.filter(activity=self,
                                              is_confirmed=True).count()
        return self.max_participants - num_bookings

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
        ordering = ['date']


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    has_journal = models.BooleanField(default=False)
    needs_journal = models.BooleanField(default=False)

    def is_space_available(self):
        num_bookings = Booking.objects.filter(activity=self.activity,
                                              is_confirmed=True).count()

        return num_bookings < self.activity.max_participants

    def __str__(self):
        return f"Booking {self.id} by {self.user.email}"
        f"for {self.activity.activity_name}"


class Review(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
        )
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Review for {self.activity} by {self.user.username}"
