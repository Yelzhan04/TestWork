from Users.serializer import UserSerializers
from Users.models import Users
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()  
    serializer_class = UserSerializers



