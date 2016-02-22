from django.shortcuts import get_object_or_404, render
from crawler.models import Event
from WeekendPlanner.settings import get_env_variable

MAPS_KEY = get_env_variable('GOOGLE_MAPS_KEY')


def index(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {'event': event, 'MAPS_KEY': MAPS_KEY}
    return render(request, 'map/index.html', context)