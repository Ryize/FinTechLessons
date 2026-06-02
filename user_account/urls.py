from django.urls import path

from user_account.views import index

urlpatterns = [
    path('', index),
]

# Главный urls + urls каждой страницы
