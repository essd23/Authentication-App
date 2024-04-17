from django.shortcuts import render


def home(request):
    return render(request, 'site_view/index.html')


def about(request):
    return render(request, 'site_view/about.html')


