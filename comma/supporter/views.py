from django.shortcuts import render

# Create your views here.

def supporter_page(request):
    return render(request, 'supporter_page.html')