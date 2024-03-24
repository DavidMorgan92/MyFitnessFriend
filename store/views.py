from django.shortcuts import render
from .models import Product


def index(request):
    if request.method == 'GET':
        if 'q' in request.GET:
            products = Product.objects.filter(name__icontains=request.GET['q'])
        else:
            products = Product.objects.all()

    context = {
        'search_term': request.GET['q'] if request.GET and 'q' in request.GET else '',
        'products': list(products),
    }

    return render(request, 'store/index.html', context)
