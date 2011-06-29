from piston.resource import Resource

from django.conf import settings
from django.http import HttpResponse

default_emitter = 'json'
emitter_map = {
    'text/html':'html',
    'text/xml':'xml',
    'application/json':'json',
}
defautl_content_type = 'application/json'
enabled_emitter = settings.ENABLED_EMITTER
def get_accept_type( request):
        """
        determine emitter from the `Accept` and `Content-Type` HTTP header
        If found both, use Accept.

        Important!
        With the exception of CONTENT_LENGTH and CONTENT_TYPE, as given above,
        any HTTP headers in the request are converted to META keys by converting
        all characters to uppercase, replacing any hyphens with underscores and
        adding an HTTP_ prefix to the name
        """
        request_content_type = request.META.get('CONTENT_TYPE', None)
        accept = request.META.get('HTTP_ACCEPT', None) or request_content_type
        if accept and ';' in accept:
            accept = accept.split(';')[0]

        if accept == '*/*' :
            if request_content_type:
                return request_content_type
            else:
                return defautl_content_type

        return accept
                
class EidosResource(Resource):
    def __init__(self, handler, authentication=None):
        super(EidosResource, self).__init__(handler, authentication)
        self.handler.resource = self
        self.csrf_exempt = getattr(self.handler, 'csrf_exempt', True)

    def __call__(self, request,*args,**kwargs):
        if not self.is_acceptable(request):
            return HttpResponse( "Not Acceptable", 'text/html', 406 )
        return super(self.__class__,self).__call__(request,*args,**kwargs)
    
    @staticmethod
    def determine_emitter( request, *args, **kwargs):
        accept = get_accept_type(request)
        if accept not in emitter_map.keys():
            return default_emitter

        return emitter_map[accept]

    def is_acceptable(self,request):
        accept = get_accept_type(request)
        if accept and "," in accept:
            if "*/*" in accept: return True
            for each_accept in accept.split(","):
                if each_accept in enabled_emitter: return True
        return accept in enabled_emitter