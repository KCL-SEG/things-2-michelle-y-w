from django.shortcuts import render
from .forms import ThingForm

def home(request):
    from = ThingFrom()
    return render(request, 'home.html', {'form': form})
