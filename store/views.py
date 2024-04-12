from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.exceptions import BadRequest
from .models import Product, ProductVariant
from .forms import SearchForm, CheckoutForm


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

            paginator = Paginator(
                products, search_form.cleaned_data['items_per_page'])
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
    variant_types = [t['type']
                     for t in product.productvariant_set.values('type').distinct()]

    variants = {}
    for type in variant_types:
        variants[type] = product.productvariant_set.filter(type__exact=type)

    context = {
        'product': product,
        'variants': variants,
    }

    return render(request, 'store/details.html', context)


@require_http_methods(['POST'])
def add_to_basket(request, id):
    # Get product and a list of its variant types
    product = get_object_or_404(Product, id=id)
    variant_types = [t['type']
                     for t in product.productvariant_set.values('type').distinct()]

    #
    # Validate post parameters

    if 'count' not in request.POST:
        raise BadRequest('No value given for count parameter')
    
    count = int(request.POST['count'])

    if count < 1 or count > 99:
        raise BadRequest(f'Invalid value given for count parameter: {count}')

    # For each variant type
    for type in variant_types:
        # If there is no corresponding parameter given, raise a validation error
        if ('variant-' + type) not in request.POST:
            raise BadRequest(f'No value given for variant type {type}')

        # Get all variants of the type with the given ID
        variants = product.productvariant_set.filter(
            type__exact=type, id__exact=request.POST['variant-' + type])

        # If there are no matching variants, raise a validation error
        if len(variants) == 0:
            raise BadRequest(f'Invalid value {
                             request.POST['variant-' + type]} given for variant type {type}')

    # Construct the chosen item
    new_item = {
        'product_id': id,
        'count': count,
        'variants': {k[8:]: int(v) for k, v in request.POST.items() if k.startswith('variant-')}
    }

    # Get the basket in the session
    basket = request.session.get('basket', [])

    # Find the index of the matching item if there is already one
    existing_item_index = -1

    # For each item in the basket
    for i in range(len(basket)):
        existing_item = basket[i]

        # If the item in the basket has the same product ID
        if existing_item['product_id'] == id:
            # Presume all variants in the existing item are the same as the new item
            all_variants_match = True

            # For each variant type in the existing item
            for variant_type, variant_value in existing_item['variants'].items():
                # If the existing item's variant type is not in the new item, or the values are different
                if variant_type not in new_item['variants'] or variant_value != new_item['variants'][variant_type]:
                    all_variants_match = False
                    break

            if all_variants_match:
                for variant_type, variant_value in new_item['variants'].items():
                    if variant_type not in existing_item['variants'] or variant_value != existing_item['variants'][variant_type]:
                        all_variants_match = False
                        break

            if all_variants_match:
                existing_item_index = i
                break

    if existing_item_index > -1:
        # If there is already a matching item in the basket, raise its count
        basket[existing_item_index]['count'] += count
    else:
        # If there isn't already a matching item in the basket, add it to the basket
        basket.append(new_item)

    request.session['basket'] = basket

    messages.add_message(request, messages.INFO, f'Added {
                         product.name} to basket')

    return redirect(reverse('store_details', kwargs={'id': id}))


def basket(request):
    def product_details(basket_item):
        product = Product.objects.filter(pk=basket_item['product_id']).first()
        price_pounds = product.price_pounds

        details = {
            'product': product,
            'variants': {},
        }

        for variant_type, variant_value in basket_item['variants'].items():
            variant = ProductVariant.objects.filter(type=variant_type, pk=variant_value, product_id=basket_item['product_id']).first()
            price_pounds += variant.price_delta_pounds
            details['variants'][variant_type] = variant

        price_pounds *= basket_item['count']
        details['price_pounds'] = price_pounds
        
        return details

    basket = request.session.get('basket', [])

    context = {
        'basket': [
            {
                **item,
                **product_details(item),
            } for item in basket
        ],
    }

    context['total_price_pounds'] = sum([item['price_pounds'] for item in context['basket']])

    return render(request, 'store/basket.html', context)


def checkout(request):
    form = CheckoutForm()

    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            pass

    context = {
        'form': form,
    }

    return render(request, 'store/checkout.html', context)
