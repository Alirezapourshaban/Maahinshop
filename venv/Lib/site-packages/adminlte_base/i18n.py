import os
import gettext


def get_locale_dir():
    """Returns the path to the translation directory."""
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'translations'
    )

    if not os.path.exists(path):
        path = '/usr/share/locale'

    return path


def get_translations(languages=None, class_=None):
    """Returns the correct gettext translations"""
    if languages is not None:
        if not isinstance(languages, (tuple, list)):
            languages = [languages]
        languages = map(str, languages)

    return gettext.translation('adminlte_full', get_locale_dir(), languages,
                               class_=class_, fallback=True)
