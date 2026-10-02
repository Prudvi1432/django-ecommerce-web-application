from django.test import TestCase
from django.contrib.auth.models import User

from .models import Product, CartItem, Order


class ProductModelTest(TestCase):

    def test_product_creation(self):

        product = Product.objects.create(
            name="Test Product",
            description="Test product description",
            category="Electronics",
            price=999.00,
            stock=10
        )

        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.stock, 10)
        self.assertEqual(str(product), "Test Product")


class CartItemModelTest(TestCase):

    def test_cart_item_creation(self):

        user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        product = Product.objects.create(
            name="Test Phone",
            description="Test phone",
            category="Electronics",
            price=15000.00,
            stock=5
        )

        cart_item = CartItem.objects.create(
            user=user,
            product=product,
            quantity=2
        )

        self.assertEqual(cart_item.quantity, 2)
        self.assertEqual(cart_item.user.username, "testuser")
        self.assertEqual(cart_item.product.name, "Test Phone")


class OrderModelTest(TestCase):

    def test_order_creation(self):

        user = User.objects.create_user(
            username="orderuser",
            password="testpassword"
        )

        order = Order.objects.create(
            user=user,
            name="Test Customer",
            email="test@example.com",
            phone="9876543210",
            address="Hyderabad",
            total_amount=1999.00,
            payment_method="Cash on Delivery"
        )

        self.assertEqual(order.name, "Test Customer")
        self.assertEqual(order.status, "Pending")
        self.assertEqual(
            order.payment_method,
            "Cash on Delivery"
        )