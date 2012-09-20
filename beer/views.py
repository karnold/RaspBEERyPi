from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson
from beer.models import Reading, Batch
from beer import sensors

def current_reading(request):
    s = sensors.sensors()
    temperature = s.readTemp()
    data = {
        'c': temperature,
        'f': s.tempFahrenheit(temperature),
        'gravity': 0
    }

    return HttpResponse(simplejson.dumps(data), mimetype='application/json')
    
