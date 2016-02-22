from django.shortcuts import render
from .models import Event


def index(request):
    e = Event()
    e.parse_through_listing_timeout('http://www.timeout.jp/tokyo/ja/%E3%83%AC%E3%82%B9%E3%83%88%E3%83%A9%E3%83%B3/%E3%83%9E%E3%83%83%E3%82%AF%E3%82%B9-%E3%83%96%E3%83%AC%E3%83%8A%E3%83%BC-%E3%83%81%E3%83%A7%E3%82%B3%E3%83%AC%E3%83%BC%E3%83%88%E3%83%90%E3%83%BC-%E8%A1%A8%E5%8F%82%E9%81%93%E3%83%92%E3%83%AB%E3%82%BA')
    existing = Event.objects.filter(title=e.title)
    if existing:
        context = { 'event': "already in database"}
    else:
        e.save()
        context = {'event': e }
    return render(request, 'crawler/index.html', context)