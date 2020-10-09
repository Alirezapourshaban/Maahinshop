"""
A basic package to simplify the integration of AdminLTE with other frameworks.
"""

from abc import ABCMeta, abstractmethod
import copy
from functools import partial

from jinja2 import Markup

from .constants import *
from .data_types import *
from .decorators import *
from .exceptions import *
from .i18n import get_translations
from .mixins import *


class MenuLoader(metaclass=ABCMeta):
    """
    A menu loader from a database or other source.

    Attributes:
        manager (Manager): Manager for accessing AdminLTE features.
        context (mixed): An abstract context object.
    """

    __slots__ = ('manager', 'context')

    def __init__(self, manager, context=None):
        """
        Arguments:
            manager (Manager): Manager for accessing AdminLTE features.
            context (mixed): An abstract context object.
        """
        self.manager = manager
        self.context = context

    def _create(self, data, active_path=None):
        """Creates and returns a menu object."""
        menu = Menu()
        items = sorted(
            data.get_items(),
            key=lambda v: (v.get_parent_id() or 0, v.get_pos(), v.get_id())
        )

        for i in items:
            menu.add_item(MenuItem(
                id_item=i.get_id(),
                title=i.get_title(),
                url=i.get_url() or self.manager.create_url(
                    i.get_endpoint(), *i.get_endpoint_args(), **i.get_endpoint_kwargs()
                ),
                parent=menu.get_item(i.get_parent_id()),
                item_type=i.get_type(),
                icon=i.get_icon(),
                help=i.get_hint()
            ))

        if active_path is not None:
            menu.activate_by_path(active_path)

        return menu

    def navbar_menu(self):
        """Creates and returns a navbar menu."""
        return None

    def sidebar_menu(self):
        """Creates and returns a sidebar menu."""
        return None


class AbstractManager(metaclass=ABCMeta):
    __slots__ = (
        '_languages_callback',
        '_home_page_callback',
        '_locale_callback',
        '_menu_loader',
        '_messages_callback',
        '_notifications_callback',
        '_tasks_callback',
        '_user_callback',
        'context',
        'default_locale',
        'home_page',
    )

    def __init__(self, context=None, default_locale=None):
        """
        Arguments:
            context (mixed): An abstract context object.
            default_locale (str): The default language.
        """
        self._languages_callback = None
        self._home_page_callback = None
        self._locale_callback = None
        self._menu_loader = None
        self._messages_callback = None
        self._notifications_callback = None
        self._tasks_callback = None
        self._user_callback = None
        self.home_page = None
        self.context = context
        self.default_locale = default_locale

    def with_context(self, context):
        """
        Arguments:
            context (mixed): An abstract context object, maybe anything,
                             is passed automatically to all callback functions
                             if passed to the constructor.
        """
        clone = copy.copy(self)
        clone.context = context
        return clone

    def _get_callback(self, name):
        callback = getattr(self, name)

        if callback is None:
            return None

        if self.context is None:
            return callback

        return partial(callback, context=self.context)

    @abstractmethod
    def create_url(self, endpoint, *endpoint_args, **endpoint_kwargs):
        """Creates and returns a URL using the address generation system of a specific framework."""
        raise NotImplementedError

    def get_available_languages(self, as_dict=False):
        """
        Normalizes and returns a dictionary with a list of available languages.

        Raises:
            adminlte_base.exceptions.Error: If the language loader is not installed..
        """
        callback = self._get_callback('_languages_callback')

        if callback is None:
            raise exceptions.Error('Missing languages_loader.')

        languages = callback()

        if isinstance(languages, dict):
            languages = languages.items()

        if as_dict:
            return {locale: name for locale, name in languages}

        return languages

    def get_flash_messages(self):
        """Creates and returns all pop-up messages by category."""
        raise NotImplementedError

    @return_namedtuple('HomeUrl', 'url', 'title')
    def get_home_page(self):
        """Returns a link to the home page as a named tuple with url and title fields."""
        callback = self._get_callback('_home_page_callback')

        if callback is not None:
            return callback()

        if self.home_page is None:
            self.home_page = ('/', 'Home')

        return self.home_page

    def get_incoming_messages(self):
        """Creates and returns a drop-down list of incoming messages."""
        callback = self._get_callback('_messages_callback')

        if callback is None:
            raise exceptions.Error('Missing messages_loader.')

        messages = callback()

        if not isinstance(messages, Dropdown):
            raise exceptions.Error(f'{type(messages).__name__} unsupported return type for messages_loader; Dropdown required.')

        return messages

    def get_locale(self):
        """Returns the current language code for current locale if `locale_getter` is set."""
        callback = self._get_callback('_locale_callback')
        locale = None

        if callback is not None:
            locale = callback()

        return locale or self.default_locale

    def get_notifications(self):
        """Creates and returns a drop-down list of notifications."""
        callback = self._get_callback('_notifications_callback')

        if callback is None:
            raise exceptions.Error('Missing notifications_loader.')

        notifications = callback()

        if not isinstance(notifications, Dropdown):
            raise exceptions.Error(f'{type(notifications).__name__} unsupported return type for notifications_loader; Dropdown required.')

        return notifications

    def get_tasks(self):
        """Creates and returns a drop-down list of assigned or executable tasks."""
        callback = self._get_callback('_tasks_callback')

        if callback is None:
            raise exceptions.Error('Missing tasks_loader.')

        tasks = callback()

        if not isinstance(tasks, Dropdown):
            raise exceptions.Error(
                f'{type(tasks).__name__} unsupported return type for tasks_loader; Dropdown required.')

        return tasks

    def get_translations(self):
        """Returns the correct gettext translations"""
        return get_translations(self.get_locale())

    def gettext(self, message, **variables):
        """
        Get a translation for the given message.

        Arguments:
            message (str): A unicode string to be translated.
        """
        return Markup(self.get_translations().gettext(message) % variables)

    def home_page_getter(self, callback):
        """
        This sets a callback to get the home page.

        Arguments:
            callback (callable): callback to get the home page.
        """
        self._home_page_callback = callback
        return callback

    def languages_loader(self, callback):
        """
        This sets the callback for loading available languages.

        Arguments:
            callback (callable): callback to get available languages.

        Examples:
            A dictionary where the key is the name of the locale and the value is the human-readable name::

                @manager.languages_loader
                def load_languages():
                    return {
                        'ru_RU': 'Русский',
                        'uk_UA': 'Українська',
                        'en_US': 'English',
                    }

            A tuple or list of pairs,
            where the first element of the pair is the locale name
            and the second element of the pair is a human-readable name::

                @manager.languages_loader
                def load_languages():
                    return (
                        ('ru_RU', 'Русский'),
                        ('uk_UA', 'Українська'),
                        ('en_US', 'English'),
                    )

            A generator, where each returned item is a pair - the name of the locale, a human-readable name::

                from babel import Locale

                @manager.languages_loader
                def load_languages():
                    for l in ('ru_RU', 'uk_UA', 'ro_MD', 'en_US'):
                        yield l, Locale.parse(l).get_display_name().title()

        Returns:
            1. A dictionary where the key is the name of the locale and the value is the human-readable name.
            2. A tuple or list of pairs,
               where the first element of the pair is the locale name
               and the second element of the pair is a human-readable name.
            3. A generator, where each returned item is a pair - the name of the locale, a human-readable name.
        """
        self._languages_callback = callback
        return callback

    def locale_getter(self, callback):
        """
        This sets a callback function for current locale selection.

        The default behaves as if a function was registered that returns `None` all the time.

        Arguments:
            callback (callable): the callback to get the current locale.
        """
        self._locale_callback = callback
        return callback

    def ngettext(self, singular, plural, n, **variables):
        """
        Get a translation for a message which can be pluralized.

        Arguments:
            singular (str): The singular form of the message.
            plural (str): The plural form of the message.
            n (int): The number of elements this message is referring to.
        """
        return Markup(self.get_translations().ngettext(singular, plural, n) % variables)

    @property
    def menu(self):
        """The loader for retrieving a menu object."""
        if self._menu_loader is None:
            raise exceptions.Error('Missing menu_loader.')
        return self._menu_loader(self, context=self.context)

    def menu_loader(self, loader: MenuLoader):
        """
        This sets the callback for loading a menu from the database or other source.

        Arguments:
            loader (MenuLoader): the loader for retrieving a menu object.
        """
        self._menu_loader = loader
        return loader

    def messages_loader(self, callback):
        """
        This sets the callback for loading a messages from the database or other source.

        Arguments:
            callback (callable): callback to receive incoming messages.
        """
        self._messages_callback = callback
        return callback

    def notifications_loader(self, callback):
        """
        This sets the callback for loading a notifications from the database or other source.

        Arguments:
            callback (callable): callback to receive notifications.
        """
        self._notifications_callback = callback
        return callback

    def tasks_loader(self, callback):
        """
        This sets the callback for loading a tasks from the database or other source.

        Arguments:
            callback (callable): callback to receive tasks.
        """
        self._tasks_callback = callback
        return callback

    def static(self, filename):
        """Generates a URL to the given asset."""
        raise NotImplementedError

    @property
    def user(self):
        """Returns the current user if user_getter is set, otherwise returns None."""
        callback = self._get_callback('_user_callback')

        if callback is None:
            return None

        return User(*callback())

    def user_getter(self, callback):
        """
        This sets a callback to get the original user object.

        Callback should return a user object and, optionally,
        matching the properties of the original object with the properties of the facade.

        Arguments:
            callback (callable): callback to get the original user object.
        """
        self._user_callback = callback
        return callback
