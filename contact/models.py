from django.db import models

# Create your models here.
class userMessage(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.full_name