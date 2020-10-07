from django.shortcuts import render, redirect
from .forms import ModelDataName
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        forms = ModelDataName(request.POST)
        if forms.is_valid():
            forms.save()
            name = forms.cleaned_data.get('name')
            messages.success(request, 'Hi ' + name)
    return render(request, 'index.html', {})
