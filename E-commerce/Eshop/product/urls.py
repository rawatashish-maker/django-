from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/",views.home),
    path("cart/",views.cart),
    path("checkout/",views.checkout),
    path("order/",views.order),
    path("logout/",views.logout),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
