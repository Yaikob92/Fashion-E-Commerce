from . models import Cart, CartItem
from . views import _cart_id

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}    
    else:
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart)
             # Sum the quantities of all cart items
            cart_count = sum(cart_item.quantity for cart_item in cart_items)
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)
