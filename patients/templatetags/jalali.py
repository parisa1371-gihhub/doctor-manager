from datetime import datetime, date
from django import template

try:
    # jdatetime is a lightweight library for Jalali conversion
    import jdatetime
except Exception:  # pragma: no cover
    jdatetime = None

register = template.Library()


def _to_datetime(value):
    if isinstance(value, datetime):
        return value
    if isinstance(value, date):
        return datetime(value.year, value.month, value.day)
    return None


@register.filter(name="jalali")
def jalali(value, fmt: str = "%Y/%m/%d"):
    """Convert Gregorian date/datetime to Jalali (Persian) string.
    If value is already a Jalali date string, return it as is.

    Usage in templates:
        {{ some_date|jalali }}
        {{ some_datetime|jalali:"%Y/%m/%d - %H:%M" }}
    """
    if value in (None, ""):
        return ""

    # If it's already a Jalali date string (YYYY/MM/DD format), return as is
    if isinstance(value, str):
        # Check if it's already in Jalali format (YYYY/MM/DD)
        if value.count('/') == 2 and len(value.split('/')) == 3:
            try:
                parts = value.split('/')
                if len(parts[0]) == 4 and len(parts[1]) == 2 and len(parts[2]) == 2:
                    # Validate that it's actually a Jalali date
                    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
                    if 1300 <= year <= 1500 and 1 <= month <= 12 and 1 <= day <= 31:
                        return value  # Already in Jalali format
            except (ValueError, IndexError):
                pass

    dt = _to_datetime(value)
    if not dt:
        return value

    if jdatetime is None:
        # Fallback to Django formatting if library is missing
        return dt.strftime(fmt)

    jdt = jdatetime.datetime.fromgregorian(datetime=dt)
    return jdt.strftime(fmt)


