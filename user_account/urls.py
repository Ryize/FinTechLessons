from django.urls import path

from user_account.views import index, products

urlpatterns = [
    path('', index),
    path('products/', products),
]

# Главный urls + urls каждой страницы
