from django.db import models


class House(models.Model):
    home_owner = models.ForeignKey("Users.Users", on_delete=models.CASCADE)
    home_price = models.IntegerField(null=True)
    home_type = models.ForeignKey("Type.HouseType", on_delete=models.CASCADE)
    home_room = models.IntegerField(null=True)
    home_address = models.CharField(max_length=50)
    home_description = models.TextField(null=True)

    def __str__(self):
        return self.home_address
