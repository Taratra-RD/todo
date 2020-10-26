from django.shortcuts import render
from app1.models import MyModel
from django.http import HttpResponse

def index(request):
    model = MyModel.objects.order_by('-pub_date')[:5]
    context = {'model': model}
    return render(request, 'index.html', context)


def detail(request):
    return HttpResponse("You're looking at question." )
