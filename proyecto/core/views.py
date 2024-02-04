from django.shortcuts import render
from . import models
from . import forms 

def index(request):
    return render(request, "core/index.html")

def persona_create(request):
    if request.method == "POST":
        form = forms.PersonaForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = forms.PersonaForm()
    return render(request, "core/persona_create.html", {"form" : form })

def about(request):
    return render(request, 'core/about.html')