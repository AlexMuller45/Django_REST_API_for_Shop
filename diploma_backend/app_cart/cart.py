from decimal import Decimal
from django.conf import settings
from app_users.models import Goods, GoodsInRetailer


class Cart(object):
    pass
    # def __init__(self, request):
    #     self.session = request.session
    #     cart = self.session.get(settings.CART_SESSION_ID)
    #     if not cart:
    #         cart = self.session[settings.CART_SESSION_ID] = {}
    #     self.cart = cart
    #
    # def add(self, item, quantity=1, update_quantity=False):
    #     item_id = str(item.id)
    #     if item_id not in self.cart:
    #         self.cart[item_id] = {
    #             'product': str(item.product.id),
    #             'retailer': str(item.retailer.id),
    #             'quantity': 0,
    #             'price': str(item.price)}
    #     if update_quantity:
    #         self.cart[item_id]['quantity'] = quantity
    #     else:
    #         self.cart[item_id]['quantity'] += quantity
    #     self.save()
    #
    # def save(self):
    #     self.session[settings.CART_SESSION_ID] = self.cart
    #     self.session.modified = True
    #
    # def remove(self, item):
    #     item_id = str(item.id)
    #     if item_id in self.cart:
    #         del self.cart[item_id]
    #         self.save()
    #
    # def __iter__(self):
    #     item_ids = self.cart.keys()
    #     items = GoodsInRetailer.objects.select_related().filter(id__in=item_ids)
    #     cart = self.cart.copy()
    #     for i_item in items:
    #         cart[str(i_item.id)]['product'] = i_item.product
    #         cart[str(i_item.id)]['retailer'] = i_item.retailer
    #     for unit in cart.values():
    #         unit['price'] = Decimal(unit['price'])
    #         unit['total_price'] = unit['price'] * unit['quantity']
    #         yield unit
    #
    # def __len__(self):
    #     return sum(item['quantity'] for item in self.cart.values())
    #
    # def get_total_price(self):
    #     return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    #
    # def clear(self):
    #     del self.session[settings.CART_SESSION_ID]
    #     self.session.modified = True

