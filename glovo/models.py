from django.db import models


class Courier(models.Model):
    fullname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.fullname

