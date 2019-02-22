from django.db import models


class Users(models.Model):
    user_name = models.CharField(max_length=30)
    user_surname = models.CharField(max_length=30)
    user_phone_number = models.IntegerField(null=True)

    def __str__(self):
        return self.user_name + " " + self.user_surname
