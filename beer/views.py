from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.utils import simplejson
from beer.models import Reading, Batch
from beer import sensors

def index(request):
    t = loader.get_template('index.html')
    c = Context({
        'title': 'Current Reading',
    });

    return HttpResponse(t.render(c))    

def current_reading(request):
    s = sensors.sensors()
    temperature = s.readTemp()
    data = {
        'c': temperature,
        'f': s.tempFahrenheit(temperature),
        'gravity': 0
    }

    return HttpResponse(simplejson.dumps(data), mimetype='application/json')
    
