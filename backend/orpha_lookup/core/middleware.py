class Middleware:

    def __init__(self, get_response):
        self.get_response = get_response


class CorsMiddleware(Middleware):

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response['Access-Control-Allow-Headers'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
