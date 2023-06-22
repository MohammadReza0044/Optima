from django.db import models

from user.models import User


class Mission(models.Model):
    MISSION_CHOICES = (
        ("شرکت", "شرکت"),
        ("منزل مشتری", "منزل مشتری"),
    )

    title = models.CharField(max_length=255)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    mission_from = models.CharField(max_length=50, choices=MISSION_CHOICES)
    mission_to = models.CharField(max_length=50, choices=MISSION_CHOICES)
    description = models.TextField()
    mission_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Mission"

    def __str__(self):
        return self.title
