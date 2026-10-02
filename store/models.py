from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    class Category(models.TextChoices):
        ELECTRONICS = 'Electronics', 'Electronics'
        CLOTHING = 'Clothing', 'Clothing'
        SHOES = 'Shoes', 'Shoes'
        ACCESSORIES = 'Accessories', 'Accessories'
        HOME_KITCHEN = 'Home & Kitchen', 'Home & Kitchen'

    name = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=Category,
        default=Category.ELECTRONICS
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class CartItem(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    def __str__(self):
        return (
            f"{self.user.username if self.user else 'No User'} "
            f"- {self.product.name} "
            f"- {self.quantity}"
        )


class Order(models.Model):

    class OrderStatus(models.TextChoices):

        PENDING = 'Pending', 'Pending'

        PROCESSING = 'Processing', 'Processing'

        SHIPPED = 'Shipped', 'Shipped'

        DELIVERED = 'Delivered', 'Delivered'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=200
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20
    )

    address = models.TextField()

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=OrderStatus,
        default=OrderStatus.PENDING
    )

    payment_method = models.CharField(
        max_length=50,
        default='Cash on Delivery'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order #{self.id} - {self.name}"