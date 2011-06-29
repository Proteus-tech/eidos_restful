#!/usr/bin/env python

from django.http import HttpResponse
from django.forms.util import ErrorDict
from django.utils.encoding import force_unicode

from piston import utils as piston_utils
from piston.emitters import Emitter
from piston.handler import typemapper
from piston.utils import HttpStatusCode
from restful.resource import EidosResource



def dictFromErrorDict(errordict):
    errors = {}
    for key, error_list in errordict.items():
        errors[key] = [force_unicode(e) for e in error_list]
    return errors

class EidosReturnCode(HttpResponse):
    def __call__(self, request, result, handler):
        if isinstance(result, ErrorDict):
            result = dictFromErrorDict(result)

        resource = handler.resource

        em_format = resource.determine_emitter(request)
        emitter, ct = Emitter.get(em_format)

        srl = emitter(result, typemapper, handler, handler.fields, anonymous=True)

        try:
            if resource.stream:
                stream = srl.stream_render(request)
            else:
                stream = srl.render(request)

            self.__init__(stream, mimetype=ct)
            self.streaming = resource.stream

        except HttpStatusCode, e:
            return e.response

        return self




content_type_map = {
    'text/html': '%s' ,
    'text/xml':'%s' ,
    'application/json': '"%s"',
}
default_content_type = 'application/json'
class EidosRCFactory(piston_utils.rc_factory):
    request = ''

    CODES = dict(ALL_OK = ('OK', 200),
                 CREATED = ('Created', 201),
                 DELETED = ('', 204), # 204 says "Don't send a body!"
                 BAD_REQUEST = ('Bad Request', 400),
                 FORBIDDEN = ('Forbidden', 403),
                 NOT_FOUND = ('Not Found', 404),
                 DUPLICATE_ENTRY = ('Conflict/Duplicate', 409),
                 NOT_HERE = ('Gone', 410),
                 NOT_IMPLEMENTED = ('Not Implemented', 501),
                 THROTTLED = ('Throttled', 503))

    def get_content_type(self, request):
        accept = request.META.get('HTTP_ACCEPT', None) or \
            request.META.get('CONTENT_TYPE', None)

        if accept and ';' in accept:
            accept = accept.split(';')[0]

        if accept not in content_type_map.keys():
            return default_content_type

        return accept

    def __getattr__(self, attr ):
        try:
            (r, c) = self.CODES.get(attr)
        except TypeError:
            raise AttributeError(attr)
        content_type = 'text/plain'
        if self.request:
            content_type = self.get_content_type( self.request )
            r = content_type_map[content_type] % ( r )
        return EidosReturnCode(r, content_type=content_type, status=c)

rc = EidosRCFactory()
