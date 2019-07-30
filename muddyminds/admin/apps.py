from django.apps import AppConfig

class CorsMiddleware(object):
    def process_response(self, req, resp):
        response["Access-Control-Allow-Origin"] = "*"
        return response

class AdminConfig(AppConfig):
    name = 'admin'
