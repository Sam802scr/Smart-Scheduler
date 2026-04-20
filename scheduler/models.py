from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()  # minutes
    deadline = models.DateTimeField()
    priority = models.IntegerField(default=1)
    scheduled = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Schedule(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
