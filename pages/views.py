from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

from .models import Design, Designer

def index(request):
    Designs=Design.objects.order_by('-date')

    paginator = Paginator(Designs,20)
    page = request.GET.get('page')
    paged_Design = paginator.get_page(page)

    context = {
        'Designs' : paged_Design
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def item(request, client):
    item = get_object_or_404(Design, client=client)

    context={
        'item' : item
    }

    return render(request, 'pages/item.html', context)

def designer(request, designer_name):

    Designers=get_object_or_404(Designer, name=designer_name)
    Designs=Design.objects.filter(designer=Designers)

    paginator = Paginator(Designs,20)
    page = request.GET.get('page')
    paged_Design = paginator.get_page(page)

    context = {
        'Designs' : paged_Design,
        'Designer' : Designers
    }

    return render(request, 'pages/designer.html', context)