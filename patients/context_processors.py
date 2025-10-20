from .models import Notification

def notifications_context(request):
    """Add notifications to all templates"""
    unread_count = Notification.objects.filter(is_read=False).count()
    return {
        'unread_notifications_count': unread_count,
    }
