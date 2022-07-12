from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"all_pages/index.html")

def about(request):
    return render(request,"all_pages/about.html")

def blog(request):
    return render(request,"all_pages/blog.html")

def portfoliyo(request):
    return render(request,"all_pages/portfoliyo.html")

def contact(request):
    return render(request,"all_pages/contact.html")

def blog_details(request):
    return render(request,"all_pages/blog_details.html")