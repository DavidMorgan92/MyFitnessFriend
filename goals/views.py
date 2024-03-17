from django.shortcuts import render
from allauth.account.decorators import login_required


@login_required
def index(request):
    return render(request, 'goals/index.html')
