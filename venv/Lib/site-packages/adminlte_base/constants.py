"""
Contains all the constant values used in the library.
"""

__all__ = (
    'FlashedMessageLevel', 'ThemeLayout', 'ThemeColor', 'DEFAULT_SETTINGS',
)


class FlashedMessageLevel(object):
    """Flash message levels"""
    DEBUG = 'debug'
    ERROR = 'error'
    WARNING = 'warning'
    INFO = 'info'
    SUCCESS = 'success'
    MESSAGE = 'message'


class ThemeLayout(object):
    """Layout Options"""
    DEFAULT = frozenset({'sidebar-mini'})
    BOXED = frozenset({'layout-boxed'}) # fixme: пропала тень справа
    COLLAPSED_SIDEBAR = frozenset({'sidebar-collapse'})
    FIXED_FOOTER = frozenset({'layout-footer-fixed'})
    FIXED_SIDEBAR = frozenset({'layout-fixed'})
    FIXED_TOP_NAV = frozenset({'layout-navbar-fixed'})
    TOP_NAV = frozenset({'layout-top-nav'})


class ThemeColor(object):
    """Color styles."""

    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    INFO = 'info'
    SUCCESS = 'success'
    WARNING = 'warning'
    DANGER = 'danger'

    WHITE = 'white'
    BLACK = 'black'
    GRAY_DARK = 'gray-dark'
    GRAY = 'gray'
    LIGHT = 'light'

    INDIGO = 'indigo'
    LIGHTBLUE = 'lightblue'
    NAVY = 'navy'
    PURPLE = 'purple'
    FUCHSIA = 'fuchsia'
    PINK = 'pink'
    MAROON = 'maroon'
    ORANGE = 'orange'
    LIME = 'lime'
    TEAL = 'teal'
    OLIVE = 'olive'

    GRADIENT_PRIMARY = 'gradient-primary'
    GRADIENT_SUCCESS = 'gradient-success'
    GRADIENT_DANGER = 'gradient-danger'
    GRADIENT_WARNING = 'gradient-warning'
    GRADIENT_INFO = 'gradient-info'


DEFAULT_SETTINGS = {
    'ADMINLTE_ACCENT_COLOR': None,
    'ADMINLTE_BACK_TO_TOP_ENABLED': False,
    'ADMINLTE_BODY_SMALL_TEXT': False,
    'ADMINLTE_DEFAULT_LOCALE': None,
    'ADMINLTE_FOOTER_SMALL_TEXT': False,
    'ADMINLTE_HOME_PAGE': ('/', 'Home'),
    'ADMINLTE_LAYOUT': ThemeLayout.DEFAULT,
    'ADMINLTE_LEGACY_USER_MENU': False,
    'ADMINLTE_SITE_TITLE': 'AdminLTE 3',
    'ADMINLTE_USER_MAPPING': {},

    'ADMINLTE_BRAND_COLOR': None,
    'ADMINLTE_BRAND_IMAGE_ALT': 'AdminLTE Logo',
    'ADMINLTE_BRAND_TEXT': 'AdminLTE 3',
    'ADMINLTE_BRAND_HTML': '<b>Admin</b>LTE 3',
    'ADMINLTE_BRAND_SMALL_TEXT': False,

    'ADMINLTE_NAVBAR_COLOR': ThemeColor.WHITE,
    'ADMINLTE_NAVBAR_NO_BORDER': False,
    'ADMINLTE_NAVBAR_SMALL_TEXT': False,

    'ADMINLTE_MAIN_SIDEBAR_ENABLED': True,
    'ADMINLTE_SECOND_SIDEBAR_ENABLED': False,
    'ADMINLTE_SIDEBAR_COLOR': ThemeColor.PRIMARY,
    'ADMINLTE_SIDEBAR_LIGHT': False,
    'ADMINLTE_SIDEBAR_CHILD_INDENT': False,
    'ADMINLTE_SIDEBAR_COMPACT': False,
    'ADMINLTE_SIDEBAR_FLAT_STYLE': False,
    'ADMINLTE_SIDEBAR_LEGACY_STYLE': False,
    'ADMINLTE_SIDEBAR_SMALL_TEXT': False,

    'ADMINLTE_ALLOW_REGISTRATION': True,
    'ADMINLTE_ALLOW_SOCIAL_AUTH': False,
    'ADMINLTE_REMEMBER_ME': False,
    'ADMINLTE_ALLOW_PASSWORD_RESET': True,
    'ADMINLTE_LANGUAGE_SWITCHER_ENABLED': False,
    'ADMINLTE_MESSAGES_ENABLED': False,
    'ADMINLTE_NOTIFICATIONS_ENABLED': False,
    'ADMINLTE_SEARCH_ENABLED': False,
    'ADMINLTE_TASKS_ENABLED': False,

    'ADMINLTE_CHANGE_LANGUAGE_ENDPOINT': 'change_language',
    'ADMINLTE_PROFILE_ENDPOINT': 'profile',
    'ADMINLTE_SEARCH_ENDPOINT': 'search',
    'ADMINLTE_TERMS_ENDPOINT': None,
    'ADMINLTE_REGISTRATION_ENDPOINT': 'auth.registration',
    'ADMINLTE_LOGIN_ENDPOINT': 'auth.login',
    'ADMINLTE_LOGOUT_ENDPOINT': 'auth.logout',
    'ADMINLTE_CHANGE_PASSWORD_ENDPOINT': 'auth.change_password',
    'ADMINLTE_PASSWORD_RESET_ENDPOINT': 'auth.reset_password',
    'ADMINLTE_PASSWORD_RECOVER_ENDPOINT': 'auth.recover_password',
}
