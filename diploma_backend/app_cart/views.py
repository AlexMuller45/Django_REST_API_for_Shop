from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, get_object_or_404
from rest_framework.response import Response

from app_megano.models import Products, Category
from app_cart.models import CartItems
from app_cart.CartServices import CartService
from app_cart.serializers import CartSerializer


class CartView(ListAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated, )
    queryset = CartItems.objects.select_related().all()

    # def get_queryset(self):
    #     return (
    #         CartItems.objects
    #         .filter(user=self.request.user)
    #         .select_related('item_id')
    #     )


# class CartItemAddView(CreateAPIView):
#     serializer_class = CartItemAddSerializer
#     permission_classes = (IsAuthenticated, )
#
#     def get_queryset(self):
#         return (
#             CartItems.objects
#             .filter(user=self.request.user)
#         )
#
# class CartItemDelView(DestroyAPIView):
#     permission_classes = (IsAuthenticated, )
#
#     def get_queryset(self):
#         return (
#             CartItems.objects
#             .filter(user=self.request.user)
#         )
#
#     def delete(self, request, pk, format=None):
#         user = request.user
#         cart_item = CartItems.objects.filter(user=user)
#         target_product = get_object_or_404(cart_item, pk=pk)
#         product = get_object_or_404(Products, id=target_product.product.id)
#         product.quantity = product.quantity + target_product.quantity
#         product.save()
#         target_product.delete()
#         return Response(status=status.HTTP_200_OK, data={"detail": "deleted"})


    # def to_representation(self, instance):
    #     # this would have the same as body as in a SerializerMethodField
    #     return 'my logic here'
    #
    # def to_internal_value(self, data):
    #     # This must return a dictionary that will be used to
    #     # update the caller's validation data, i.e. if the result
    #     # produced should just be set back into the field that this
    #     # serializer is set to, return the following:
    #     return {
    #       self.field_name: 'Any python object made with data: %s' % data
    #     }