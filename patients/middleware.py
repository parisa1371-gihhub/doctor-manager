from django.utils import translation
from django.conf import settings


class LanguageMiddleware:
    """Middleware to set language based on user session"""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get language from session, default to 'fa'
        language = request.session.get('language', 'fa')
        
        # Set the language for this request
        if language in ['fa', 'en']:
            translation.activate(language)
            request.LANGUAGE_CODE = language
        
        response = self.get_response(request)
        
        # Deactivate translation after response
        translation.deactivate()
        
        return response
