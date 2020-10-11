from django.shortcuts import render

# Create your views here.
def class_page(request):
    return render(request, 'class_page.html')

def program_form(request):
    return render(request, 'program_form.html')

def class_detail(request):
    return render(request, 'class_detail.html')