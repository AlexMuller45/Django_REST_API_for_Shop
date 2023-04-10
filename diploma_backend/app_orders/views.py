from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action

from app_orders.serializers import OrdersSerializer, CreateOrderSerializer

from app_orders.models import Orders, ProductInOrder
from app_users.models import UserProfile
from app_megano.models import Products


class OrdersViewSet(viewsets.ViewSet):
    serializer_class = OrdersSerializer
    permission_classes = (IsAuthenticated, )
    parser_classes = [JSONParser]

    def get_queryset(self):
        return (
            Orders.objects
            .select_related()
            .prefetch_related()
            .filter(user_profile__user=self.request.user)
            .order_by('-createdAt')
        )

    def list(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateOrderSerializer(data=request.data, many=True)
        # serializer.is_valid(raise_exception=True)
        data = request.data
        profile = UserProfile.objects.get(user=request.user)

        new_order = Orders.objects.create(user_profile=profile)

        for i_item in data:
            product = Products.objects.get(id=int(i_item['id']))
            item = ProductInOrder.objects.create(
                    order=new_order,
                    product=product,
                    price=i_item['price'],
                    count=i_item['count']
            )
            item.save()

        new_order.totalCost = new_order.get_total_cost()
        new_order.save()

        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)
