from django.http import Http404
from app_megano.models import Products
from .models import CartItems


class CartService:
    """
    Сервис корзины
    add_items: добавление товара в корзину
    remove_items: удаление товара из корзины
    get_items: получение списка товаров в корзине
    """
    def add_items(self, item_id, count=1, update_count=False):
        """
        Добавление товара в корзину
        :param item_id: int
        :param count: int
        :param update_count: Bool
        """
        product = Products.objects.get(id=item_id).values('category', 'price', 'freeDelivery')
        user = self.request.user
        cart_item = CartItems.objects.filter(user=user, item_id=item_id)
        if not cart_item:
            cart_item = CartItem(
                    user=user,
                    item_id=product,
                    category=product.category,
                    price=product.price,
                    count=count,
                    freeDelivery=product.freeDelivery
            )
        if update_count:
            cart_item.count = count
        product.count -= count
        cart_item.save()
        product.save()

    def remove_items(self, item_id, count):
        """
        Удаление товара и корзины
        :param item_id: int
        :param count: int
        """
        user = self.request.user
        cart_item = CartItems.objects.filter(user=user, item_id=item_id)
        if not cart_item:
            raise Http404('Совпадений не найдено')
        if cart_item.count > count:
            cart_item.count -= count
            cart_item.save()
        else:
            cart_item.delete()

    def get_items(self):
        """
        Получение списка товаров в корзине
        :return: Queryset
        """
        return CartItems.objects.filter(user=self.request.user)

    def __len__(self):
        pass

    def get_total_price(self):
        pass

    def clear(self):
        pass

    def save(self):
        pass

    # def merge_carts(self, other):
    #     """Перенос анонимной корзины в корзину зарегистрированного"""
    #     for item in other.get_goods():
    #         self.add_to_cart(item['seller_product'], item['quantity'],)
    #     other.clear()
