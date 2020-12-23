from django import template

register = template.Library()

@register.filter(name="is_in_cart")
def is_in_cart(product,cart):
    keys = cart.keys()
    non_value=0
    for key,value in cart.items():
        if value == 0:
            non_value=key
    if non_value == 0:
        pass
    else:
        non_value=str(non_value)
        cart.pop(non_value)
        print(cart)
    for id in keys:
        if int(id) == product.id:
            return True
    return False;

@register.filter(name="cart_quantity")
def cart_quantity(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0;


@register.filter(name="price_total")
def price_total(product,cart):
    return product.price * cart_quantity(product,cart)

@register.filter(name="total_cart_price")
def total_cart_price(products,cart):
    sum = 0
    for p in products:
        sum += price_total(p,cart)
    return sum
