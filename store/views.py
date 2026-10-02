from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.core.paginator import Paginator


from .models import Product, CartItem, Order


def home(request):

    search_query = request.GET.get('search', '').strip()
    category = request.GET.get('category', '').strip()

    products = Product.objects.all()

    # Search products
    if search_query:

        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Category filter
    if category:

        products = products.filter(
            category=category
        )

    products = products.order_by('-created_at')

    paginator = Paginator(products, 8)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    categories = Product.Category.choices

    return render(
        request,
        'home.html',
        {
            'products': page_obj,
            'page_obj': page_obj,
            'search_query': search_query,
            'category': category,
            'categories': categories
        }
    )


def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    return render(
        request,
        'product_detail.html',
        {
            'product': product
        }
    )


@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    # Prevent adding an out-of-stock product
    if product.stock < 1:

        return redirect(
            'product_detail',
            product_id=product.id
        )

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={
            'quantity': 1
        }
    )

    if not created:

        if cart_item.quantity < product.stock:

            cart_item.quantity += 1
            cart_item.save()

        else:

            return redirect('cart')

    return redirect('cart')


@login_required
def cart(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    )

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    return render(
        request,
        'cart.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )


@login_required
def remove_from_cart(request, item_id):

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    cart_item.delete()

    return redirect('cart')


@login_required
def increase_quantity(request, item_id):

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    if cart_item.quantity < cart_item.product.stock:

        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def decrease_quantity(request, item_id):

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    if cart_item.quantity > 1:

        cart_item.quantity -= 1
        cart_item.save()

    else:

        cart_item.delete()

    return redirect('cart')


@login_required
def checkout(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    )

    if not cart_items.exists():

        return redirect('cart')

    total = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    # Check stock before displaying checkout
    for item in cart_items:

        if item.quantity > item.product.stock:

            return render(
                request,
                'checkout.html',
                {
                    'cart_items': cart_items,
                    'total': total,
                    'error': (
                        f'Not enough stock available for '
                        f'{item.product.name}.'
                    )
                }
            )

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()

        email = request.POST.get('email', '').strip()

        phone = request.POST.get('phone', '').strip()

        address = request.POST.get('address', '').strip()

        payment_method = request.POST.get(
            'payment_method',
            ''
        ).strip()


        # Validate name
        if not name:

            return render(
                request,
                'checkout.html',
                {
                    'cart_items': cart_items,
                    'total': total,
                    'error': 'Please enter your full name.'
                }
            )


        # Validate email
        if not email or '@' not in email:

            return render(
                request,
                'checkout.html',
                {
                    'cart_items': cart_items,
                    'total': total,
                    'error': 'Please enter a valid email address.'
                }
            )


        # Validate phone
        if not phone:

            return render(
                request,
                'checkout.html',
                {
                    'cart_items': cart_items,
                    'total': total,
                    'error': 'Please enter your phone number.'
                }
            )


        if not phone.isdigit() or len(phone) != 10:

            return render(
                request,
                'checkout.html',
                {
                    'cart_items': cart_items,
                    'total': total,
                    'error': (
                        'Please enter a valid 10-digit phone number.'
                    )
                }
            )


        # Validate address
        if not address:

            return render(
                request,
                'checkout.html',
                {
                    'cart_items': cart_items,
                    'total': total,
                    'error': 'Please enter your delivery address.'
                }
            )


        # Validate payment method
        if payment_method != 'Cash on Delivery':

            return render(
                request,
                'checkout.html',
                {
                    'cart_items': cart_items,
                    'total': total,
                    'error': 'Please select a valid payment method.'
                }
            )


        # Final stock check before creating order
        for item in cart_items:

            if item.quantity > item.product.stock:

                return render(
                    request,
                    'checkout.html',
                    {
                        'cart_items': cart_items,
                        'total': total,
                        'error': (
                            f'Stock changed for '
                            f'{item.product.name}. '
                            f'Please update your cart.'
                        )
                    }
                )


        # Create order and update stock together
        with transaction.atomic():

            for item in cart_items:

                product = item.product

                product.stock -= item.quantity

                product.save()


            order = Order.objects.create(
                user=request.user,
                name=name,
                email=email,
                phone=phone,
                address=address,
                total_amount=total,
                payment_method=payment_method
            )


            cart_items.delete()


        return render(
            request,
            'order_success.html',
            {
                'order': order
            }
        )


    return render(
        request,
        'checkout.html',
        {
            'cart_items': cart_items,
            'total': total
        }
    )


@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'my_orders.html',
        {
            'orders': orders
        }
    )