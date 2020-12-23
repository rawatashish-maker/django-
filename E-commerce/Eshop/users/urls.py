from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
        

urlpatterns = [
    path("register/",views.register),
    path("afterregister/",views.afterregister),
    path("login/",views.login)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)