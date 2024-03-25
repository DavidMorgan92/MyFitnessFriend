from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product
from .forms import SearchForm


def index(request):
    return render(request, 'store/index.html')


def search(request):
    search_form = SearchForm(request.GET)
    
    paginator = None
    page = None

    if request.method == 'GET':
        if search_form.is_valid():
            products = Product.objects.filter(name__icontains=search_form.cleaned_data['search_term']).order_by(
                search_form.cleaned_data['sort_order'])

            paginator = Paginator(products, search_form.cleaned_data['items_per_page'])
            page = paginator.get_page(search_form.cleaned_data['page'])

    context = {
        'search_form': search_form,
        'count': paginator.count if paginator else None,
        'page': page,
        'page_range': range(1, paginator.num_pages + 1) if paginator else None,
    }

    return render(request, 'store/search.html', context)


def details(request, id):
    product = get_object_or_404(Product, id=id)

    context = {
        'product': product,
    }

    return render(request, 'store/details.html', context)