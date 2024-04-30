from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return str(self.title) + " - " + self.creation_date.strftime("%d/%m/%Y, %H:%M:%S")