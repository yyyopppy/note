from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import CustomUser
# class CustomUserAdmin(admin.ModelAdmin):
#     add_form = CustomUserCreationForm  # カスタムのユーザー作成フォームを指定
#     model = CustomUser

#     list_display = ('id', 'username', 'is_staff')
#     list_display_links =  ('id', 'username', 'is_staff')
admin.site.register(CustomUser, UserAdmin)