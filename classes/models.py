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
    locaton = models.CharField(max_length=200)
    max_participants = models.PositiveIntegerField(default=10)
    current_participants = models.PositiveIntegerField(default=0)
    type_choices = [
        ('Course', 'Class'),
        ('Group Counseling', 'Group Counseling'),
        ('Yoga Session', 'Yoga Session'),
    ]
    type = models.CharField(
        max_length=20,
        choices=type_choices,
        default='Course',
        )

    def __str__(self):
        return f"{self.name} on {self.date}"

    def is_full(self):
        if not activity.is_full:
            # users must sign up, when they book each activity,
            # it will increement until capacity is reached
            activity.current_participants += 1
            activity.save()
        else:
            pass

        return f"{self.current_participants}"

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
        ordering = ['date']


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
