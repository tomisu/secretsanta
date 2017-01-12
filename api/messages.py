from django.core import serializers
from django.http import  HttpResponse
import json


class message:
    """
    API messages
    """
    def success(*args):
        message = {}
        if len(args) > 0: message['data'] = args[0]
        message['status']= "OK"

        return HttpResponse(json.dumps(message), content_type='application/json')


    def error(exception):
        message = {
            'status': "ERROR",
            'description': exception.__name__,
        }
        return HttpResponse(json.dumps(message), content_type='application/json')
