from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, get_object_or_404
from rest_framework.response import Response

from app_megano.models import Products, Category
from .models import CartItems
from app_cart.CartServices import CartService
from app_cart.serializers import CartSerializer


class CartView(ListAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return (
            CartItems.objects
            .filter(user=self.request.user)
        )


class CartItemAddView(CreateAPIView):
    queryset = CartItems.objects.filter(user=self.request.user)
    serializer_class = CartItemAddSerializer
    permission_classes = (IsAuthenticated, )


class CartItemDelView(DestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = CartItems.objects.filter(user=self.request.user)

    def delete(self, request, pk, format=None):
        user = request.user
        cart_item = CartItems.objects.filter(user=user)
        target_product = get_object_or_404(cart_item, pk=pk)
        product = get_object_or_404(Products, id=target_product.product.id)
        product.quantity = product.quantity + target_product.quantity
        product.save()
        target_product.delete()
        return Response(status=status.HTTP_200_OK, data={"detail": "deleted"})
