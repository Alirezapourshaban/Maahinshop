"""
Provides ready-made implementations for filters used in templates.
"""

from string import Template

import arrow
from dateutil import tz

from .constants import ThemeColor


__all__ = ('humanize', 'if_true', 'navbar_skin', 'sidebar_skin', 'replace_with_flag')


def humanize(dt, locale='en_us', time_zone=None):
    """The filter converts the date to human readable."""
    dt = arrow.get(dt, tz.gettz(time_zone))
    return dt.humanize(locale=locale, only_distance=True)


def if_true(value, replace_with=None):
    """Replaces the value with the passed if the value is true."""
    if not value:
        return ''

    if replace_with is None:
        return value

    return Template(replace_with).safe_substitute(value=value)


def replace_with_flag(locale):
    """The filter replaces the locale with the CSS flag classes of the flag-icon-css library."""
    locale = locale.replace('-', '_').lower().rsplit('_', maxsplit=1)

    if len(locale) == 2:
        return f'flag-icon flag-icon-{locale[-1]}'

    return ''


def navbar_skin(color):
    """Returns a collection of classes to style the navigation bar."""
    if color:
        light = {ThemeColor.LIGHT, ThemeColor.WARNING, ThemeColor.WHITE, ThemeColor.ORANGE}
        style = 'light' if color in light else f'dark'
        return f'navbar-{style} navbar-{color}'
    return ''


def sidebar_skin(color, light=False):
    """Returns a collection of classes to style the main sidebar bar."""
    if color:
        style = 'light' if light else f'dark'
        return f'sidebar-{style}-{color}'
    return ''
