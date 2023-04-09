from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action

from app_orders.serializers import OrdersSerializer
from app_orders.models import Orders



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
