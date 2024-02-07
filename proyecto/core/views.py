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
            messages.success(request, 'Mensaje enviado con éxito.')
            return redirect('index')
    else:
        form = forms.PersonaForm()
    return render(request, "core/persona_create.html", {"form" : form })

def about(request):
    return render(request, 'core/about.html')
from django.shortcuts import redirect
from django.contrib import messages

