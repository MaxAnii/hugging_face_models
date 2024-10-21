from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class TokenValidationMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        
        self.valid_token = 'your-secure-token-value'

    def __call__(self, request):
        
        token = request.headers.get('Authorization')

       
        if token == self.valid_token:
           
            response = self.get_response(request)
            return response
        else:
           
            return JsonResponse({'error': 'Forbidden: Invalid Token'}, status=403)
