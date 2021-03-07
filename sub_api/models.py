from django.db import models

# Create your models here.
class Subscriptions(models.Model):
    email = models.CharField(max_length=75)

    def __str__(self):
        return self.email
