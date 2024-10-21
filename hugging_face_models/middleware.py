from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
import os
class TokenValidationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        
        self.valid_token = os.getenv('SECRET_KEY')

    def __call__(self, request):
        
        token = request.headers.get('Authorization')

       
        if token == self.valid_token:
           
            response = self.get_response(request)
            return response
        else:
           
            return JsonResponse({'error': 'Forbidden: Invalid Token'}, status=403)
