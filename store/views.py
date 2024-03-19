from django.shortcuts import render
from .models import Product


def index(request):
    if request.method == 'GET':
        if 'q' in request.GET:
            products = Product.objects.filter(name_icontains=request.GET['q'])
        else:
            products = Product.objects.all()

    context = {
        'products': list(products),
    }

    return render(request, 'store/index.html', context)
