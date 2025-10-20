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

    Usage in templates:
        {{ some_date|jalali }}
        {{ some_datetime|jalali:"%Y/%m/%d - %H:%M" }}
    """
    if value in (None, ""):
        return ""

    dt = _to_datetime(value)
    if not dt:
        return value

    if jdatetime is None:
        # Fallback to Django formatting if library is missing
        return dt.strftime(fmt)

    jdt = jdatetime.datetime.fromgregorian(datetime=dt)
    return jdt.strftime(fmt)


