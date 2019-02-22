from django.db import models


class HouseType(models.Model):
    house_type = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.house_type
