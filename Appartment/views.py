import json

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Appartment.form import Sort
from Appartment.models import House
from Users.serializer import HouseSerializers


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializers

    def house_price(request):
        price = House.objects.all()
        form = Sort(request.GET)
        if form.is_valid():
            if form.cleaned_data["min_price"]:
                price = price.filter(home_price__gte=form.cleaned_data['min_price'])
            if form.cleaned_data["max_price"]:
                price = price.filter(home_price__gte=form.cleaned_data['max_price'])
            if form.cleaned_data["ordering"]:
                price = price.order_by(form.cleaned_data['ordering'])
        context={'price':price,"form":form}
        return render(request,"",context)

    @action(methods=['post'], detail=False)
    def search(self, request):
        title_data = request.data['title']
        house_list = self.queryset.filter(home_address__contains=title_data).values()
        s = json.dumps(list(house_list))
        return Response(s)
