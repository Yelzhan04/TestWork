from rest_framework import serializers
from Users.models import Users
from Appartment.models import House


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('user_name', 'user_surname', 'user_phone_number')


class HouseSerializers(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = ("url", "home_owner", "home_type", "home_address", "home_price", "home_room", "home_description")
