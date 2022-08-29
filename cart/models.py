from django.db import models

from decimal import Decimal
from django.conf import settings
from core_app.models import Phone


class Cart(models.Model):

    def __int__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, phone, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        phone_id = str(phone.id)
        if phone_id not in self.cart:
            self.cart[phone_id] = {'quantity': 0,
                                     'price': str(phone.price)}
        if update_quantity:
            self.cart[phone_id]['quantity'] = quantity
        else:
            self.cart[phone_id]['quantity'] += quantity
        self.save()

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        phone_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Phone.objects.filter(id__in=phone_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

