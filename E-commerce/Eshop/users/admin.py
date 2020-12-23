from django.contrib import admin
from users.models import UserModel

class AdminUserModel(admin.ModelAdmin):
    list_display =  ['firstname','lastname','email','password']

admin.site.register(UserModel, AdminUserModel)



# Register your models here.
