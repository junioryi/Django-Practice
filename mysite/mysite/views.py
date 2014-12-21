from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    
    now  = datetime.datetime.now()
    """
    Instead of doning the following, use shorcut render().

    t    = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

    """
    return render(request, 'current_datetime.html', {'current_date': now})
    

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    """
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" %(offset, dt)
    return HttpResponse(html)
    """
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})
