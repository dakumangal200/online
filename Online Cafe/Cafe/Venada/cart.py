from decimal import Decimal
from django.conf import settings
from Cafe_admin.models import Product


class client_Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, Product, quantity=1, update_quantity=False):
        product_id = str(Product.Product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'id': Product.Product_id, 'quantity': 0, 'price': str(Product.Price), 'name': Product.Product_Name, 'image': Product.Product_image}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, Product):
        product_id = str(Product.Product_id)
        print(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(Product_id__in=product_ids)
        for product in products:
            self.cart[str(Product.Product_id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
