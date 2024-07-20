from django.shortcuts import render, redirect
from .models import Obituary
from .forms import ObituaryForm  # Ensure you have created this form

def obituary_list(request):
    obituaries = Obituary.objects.all()
    return render(request, 'obituaries/obituary_list.html', {'obituaries': obituaries})

def submit_obituary(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('obituary_list')  # Redirect to the list after saving
    else:
        form = ObituaryForm()
    return render(request, 'obituaries/obituary_form.html', {'form': form})
