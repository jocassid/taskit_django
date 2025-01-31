
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    description = models.CharField(max_length=256)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    completed_date = models.DateTimeField(null=True, blank=True)

    priority = models.IntegerField(default=0)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks',
        null=True,
        blank=True
    )

    def  __str__(self):
        return self.description







