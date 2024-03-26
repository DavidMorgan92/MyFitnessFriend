def basket(request):
    return {
        'basket': request.session.get('basket', {}),
    }
