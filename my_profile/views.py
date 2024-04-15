from django.shortcuts import render
from allauth.account.decorators import login_required
from store.models import Order


@login_required
def index(request):
    return render(request, 'my_profile/index.html')


@login_required
def orders(request):
    orders = Order.objects.filter(owner=request.user)

    context = {
        'orders': orders,
    }

    return render(request, 'my_profile/orders.html', context)
