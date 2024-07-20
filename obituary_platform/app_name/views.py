from django.shortcuts import render, get_object_or_404
from .models import Obituary

def obituary_list(request):
    obituaries = Obituary.objects.all()
    return render(request, 'obituaries/obituary_list.html', {'obituaries': obituaries})

def obituary_detail(request, slug):
    obituary = get_object_or_404(Obituary, slug=slug)
    return render(request, 'obituaries/obituary_detail.html', {'obituary': obituary})
