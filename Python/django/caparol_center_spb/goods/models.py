from django.db import models

class Good(models.Model):
    title = models.CharField(max_length = 20)
    description = models.TextField()
    img = models.FileField()

