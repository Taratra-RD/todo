from django.shortcuts import render,get_object_or_404
from app1.models import MyModel
from django.http import HttpResponse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_title_list'

    def get_queryset(self):
        return MyModel.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = MyModel
    template_name = 'app1/detail.html'