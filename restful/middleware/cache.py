class NoCacheMiddleware(object):

    def process_response(self, request, response):

        if (request.method == 'GET' or request.method == 'PUT') and not response.has_header('Cache-Control'):
            response['Cache-Control'] = 'no-cache, no-store'

        return response
