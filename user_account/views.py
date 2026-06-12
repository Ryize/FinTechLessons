from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        print(login, password)
    return render(request, 'user_account/index.html')


def products(request):
    return render(request, 'user_account/products.html')
