from .models import Notification

def notifications_context(request):
    """Context processor for unread notifications count"""
    if request.user.is_authenticated:
        unread_notifications_count = Notification.objects.filter(is_read=False).count()
    else:
        unread_notifications_count = 0
    return {'unread_notifications_count': unread_notifications_count}


def settings_context(request):
    """Context processor for user settings"""
    if request.user.is_authenticated:
        # Get user settings from session
        current_language = request.session.get('language', 'fa')
        notifications_enabled = request.session.get('notifications_enabled', True)
        current_theme = request.session.get('theme', 'light')
        
        return {
            'current_language': current_language,
            'notifications_enabled': notifications_enabled,
            'current_theme': current_theme,
        }
    return {
        'current_language': 'fa',
        'notifications_enabled': True,
        'current_theme': 'light',
    }