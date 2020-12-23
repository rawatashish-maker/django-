from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import Product,Category,Order
from users.models import UserModel

def home(request):
    if request.session.get("email"):
        if request.method == "POST":
            product = request.POST.get('product')
            remove = request.POST.get('remove')
            cart = request.session.get('cart')
            if cart:
                quantity = cart.get(product)
                if quantity:
                    if remove:
                        cart[product] = quantity-1
                    else:
                        cart[product] = 1+quantity
                else:
                    cart[product] = 1
            else:
                cart = {}
                cart[product] = 1
            request.session['cart'] = cart
            print(request.session['cart'])

        products = None
        categories = Category.get_all_categories();
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();
        data={}
        data['products']=products
        data['categories']=categories
        return render(request,"home.html",data)
    else:
        return redirect("/users/register/")


def cart(request):
    if request.session.get("email"):
        if request.method == "GET":
            ids = list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
            return render(request,"cart.html",{'products':products})
    else:
        return redirect("/users/register/")



def checkout(request):
    if request.session.get("email"):
        if request.method == "POST":
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            custm = request.session.get("email")
            cust=UserModel.objects.get(email=custm)
            customer=cust.id
            cart = request.session.get('cart')
            products = Product.get_products_by_id(list(cart.keys()))
            for product in products:
                order = Order(customer = UserModel(id=customer),
                              product = product,
                              price = product.price,
                              address = address,
                              phone = phone,
                              quantity = cart.get(str(product.id)))
                order.save()
            request.session['cart'] = {}
            return redirect("/product/cart/")        
    else:
        return redirect("/users/register/")


def order(request):
    if request.session.get("email"):
        if request.method == "GET":
            customer_email = request.session.get("email")
            customer_Id = UserModel.objects.get(email=customer_email)
            customer= customer_Id.id
            orders = Order.get_orders_by_customer(customer)
            return render(request,"order.html",{'orders':orders})
    else:
        return redirect("/users/register/")



def logout(request):
    if request.method == "GET":
        del request.session['email']
        return redirect("/users/register/")

# Create your views here.
