from django.shortcuts import render


def index(request):
    return render(request, 'user_account/index.html')


def products(request):
    return render(request, 'user_account/products.html')
