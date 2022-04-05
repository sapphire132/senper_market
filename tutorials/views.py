from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Tutorial

def tutorials(request):
    Tutorials = Tutorial.objects.order_by('-date')

    context = {
        'Tutorials' : Tutorials
    }

    return render(request, 'tutorials/tutorial.html', context)

def tutorial(request, course_id):
    tutorial = get_object_or_404(Tutorial, pk=course_id)
    Tutorials = Tutorial.objects.order_by('-date')

    context = {
        'tutorial' : tutorial,
        'Tutorials' : Tutorials
    }

    return render(request, 'tutorials/tutorial.html', context)
