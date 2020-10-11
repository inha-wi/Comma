from django.shortcuts import render

# Create your views here.
def notice_page(request):
    return render(request, 'notice_page.html')

def inquiry(request):
    return render(request, 'inquiry.html')

def program(request):
    return render(request, 'program.html')

def supporters(request):
    return render(request, 'supporters.html')