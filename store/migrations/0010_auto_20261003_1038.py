from django.db import migrations


def create_initial_product(apps, schema_editor):

    Product = apps.get_model('store', 'Product')

    Product.objects.get_or_create(
        name='Wireless Headphones',
        defaults={
            'description': 'High quality wireless headphones',
            'category': 'Electronics',
            'price': 1999.00,
            'stock': 10,
        }
    )


def reverse_product(apps, schema_editor):

    Product = apps.get_model('store', 'Product')

    Product.objects.filter(
        name='Wireless Headphones'
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_product_category'),
    ]

    operations = [
        migrations.RunPython(
            create_initial_product,
            reverse_product
        ),
    ]