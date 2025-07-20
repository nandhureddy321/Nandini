from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Product List with Category Filter
def product_list(request):
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'product_list.html', {'products': products, 'categories': categories})

# Product Detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# Add to Cart (store as dict: {product_id: quantity})


# View Cart (reads cart from session)


# Reset Cart (for testing)
def reset_cart(request):
    request.session['cart'] = {}
    return redirect('view_cart')

# Signup View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Place Order
@login_required
def place_order(request):
    cart = request.session.get('cart', {})
    if cart:
        order = Order.objects.create(user=request.user)
        order.products.set(cart.keys())  # assuming many-to-many
        order.save()
        request.session['cart'] = {}  # clear cart
        return redirect('order_history')
    return redirect('product_list')

# Order History
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'catalog/order_history.html', {'orders': orders})





def add_to_cart(request, pk):
    cart = request.session.get('cart', {})

    # If cart is a list (old format), convert it to dict with quantities
    if isinstance(cart, list):
        cart_dict = {}
        for pid in cart:
            pid_str = str(pid)
            cart_dict[pid_str] = cart_dict.get(pid_str, 0) + 1
        cart = cart_dict

    pk = str(pk)
    cart[pk] = cart.get(pk, 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')



from django.shortcuts import render
from .models import Product

def view_cart(request):
    # Get the cart from session or empty dict if none
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(pk=product_id)
            subtotal = product.price * quantity
            total += subtotal
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })
        except Product.DoesNotExist:
            # If product was removed from DB but still in cart session, skip it
            continue

    return render(request, 'catalog/cart.html', {
        'cart_items': cart_items,
        'total': total,
    })

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(pk=product_id)
            subtotal = product.price * quantity
            total += subtotal
            products.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal,
            })
        except Product.DoesNotExist:
            continue

    return render(request, 'catalog/cart.html', {
        'cart_items': products,
        'total': total,
    })



