#from django.template.loader import get_template
# django.template import Context
#from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.conf import settings
import datetime

def homepage(request):    
    return render_to_response('home.html')

def current_datetime(request):
    #now = datetime.datetime.now()
    '''t = get_template('time/current_datetime.html')    
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)'''
    #return render_to_response('time/current_datetime.html', {'current_datetime':now})
    #settings.configure()    
    '''now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_datetime':now})'''
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())
    
'''
def display_meta(request):    
    values = request.META.items()    
    values.sort()    
    html = []    
    for k, v in values:        
        html.append('<tr><td>%s</td><td>%s</td></tr>'%(k, v)) 
        
    return HttpResponse('<table>%s</table>'%'\n'.join(html))
    
UnicodeDecodeError at /meta
'ascii' codec can't decode byte 0xa3 in position 990: ordinal not in range(128)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/meta
Django Version:	1.2.7
Exception Type:	UnicodeDecodeError
Exception Value:	
'ascii' codec can't decode byte 0xa3 in position 990: ordinal not in range(128)
    '''
#git_test