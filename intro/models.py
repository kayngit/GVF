from django.db import models
from django.utils import timezone


class Intro(models.Model):
    html = models.TextField()

    def __str__(self):
        return self.html