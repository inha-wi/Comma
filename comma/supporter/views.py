from django.shortcuts import render

# Create your views here.

def supporter_page(request):
    return render(request, 'supporter_page.html')

def supporters_form(request):
    return render(request, 'supporters_form.html')