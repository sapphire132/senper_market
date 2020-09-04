from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

from .models import Design

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


def item(request, item_id):
    item = get_object_or_404(Design, pk=item_id)

    context={
        'item' : item
    }

    return render(request, 'pages/item.html', context)