from django.shortcuts import render


def home(request):
    return render(request, 'my_website/home.html')


def resume(request):
    return render(request, 'my_website/resume.html')


def work(request):
    return render(request, 'my_website/work.html')
