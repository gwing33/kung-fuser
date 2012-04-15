from django.template import Context, loader
from django.http import HttpResponse

def index(request):
    t = loader.get_template('Home/index.html')
    
    c = Context({"my_name": "Gerald"})
    
    return HttpResponse(t.render(c))