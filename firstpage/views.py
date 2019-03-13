from django.shortcuts import render


def home(request):
    return render(request, 'firstpage/homepage.html')

def about(request):
    return render(request, 'firstpage/about.html')
