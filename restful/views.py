from django.template import RequestContext
from django.shortcuts import render_to_response

from restful import docs

def documentation_view(request):
    """
    Generates documentation from the handlers you've defined.
    """    
    context = {
        'docs':docs,
    }    
    return render_to_response('document.html',  context, RequestContext(request))