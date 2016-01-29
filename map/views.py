from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'map/index.html', context)
