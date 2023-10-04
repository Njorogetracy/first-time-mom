from django.db import models
from django.contrib.auth.models import User


class ActivityType(models.Model):
    # name = models.CharField(max_length=200, unique=True)
    # description = models.TextField(blank=True)
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

    # def __str__(self):
    #     return self.name


class Activity(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    date = models.DateTimeField()
    locaton = models.CharField(max_length=200)
    max_participants = models.PositiveIntegerField(default=10)
    current_participants = models.PositiveIntegerField(default=0)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE, null=True)  # noqa

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Review for {self.activity} by {self.user.username}"