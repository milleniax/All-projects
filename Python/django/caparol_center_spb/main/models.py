from django.db import models

class Question(models.Model):
    phone = models.CharField(max_length = 11)
    vk = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.vk