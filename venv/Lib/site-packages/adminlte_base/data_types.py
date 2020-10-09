"""
Entities used in templates.
"""

from collections import OrderedDict
from datetime import datetime

from .constants import ThemeColor, FlashedMessageLevel


__all__ = (
    'Dropdown',
    'FlashedMessage',
    'Menu',
    'MenuItem',
    'Message',
    'Notification',
    'PageItem',
    'Task',
    'User',
)


class Collection(object):
    """
    A wrapper for storing objects of the same type.

    Implements an iterator over the elements of the collection.
    """

    __slots__ = ('items',)

    def __init__(self):
        self.items = []

    def __iter__(self):
        return iter(self.items)

    def add(self, item):
        """Adds an item to the collection."""
        self.items.append(item)

    def get_total(self):
        """Returns the number of items in the collection."""
        return len(self.items)


class Dropdown(Collection):
    """Drop-down list in the upper navbar."""

    __slots__ = ('url', 'total_items')

    def __init__(self, url, total_items=None):
        """
        Arguments:
            url (str): he URL of the page where you can see all the elements of the collection.
            total_items (int): the total number of elements in the storage.
        """
        super().__init__()
        self.url = url
        self.total_items = total_items

    def get_total(self):
        """
        Returns the total number of elements in the storage,
        if the value was passed in the constructor,
        or the number of elements in the collection.
        """
        if self.total_items is None:
            return super().get_total()
        return self.total_items

    def get_url(self):
        """
        Returns the URL of the page where you can see all the elements of the collection.
        """
        return self.url


class DropdownItem(object):
    """Drop-down list item."""

    __slots__ = ('url', 'icon', 'color')

    def __init__(self, icon=None, color=None):
        """
        Arguments:
            icon (str): CSS classes for the icon.
            color (str): the color code from the theme.
        """
        self.icon = icon
        self.color = color


class FlashedMessage(object):
    """A message pop-up on the page."""

    COLOR = {
        FlashedMessageLevel.DEBUG: ThemeColor.SECONDARY,
        FlashedMessageLevel.ERROR: ThemeColor.DANGER,
        FlashedMessageLevel.WARNING: ThemeColor.WARNING,
        FlashedMessageLevel.INFO: ThemeColor.INFO,
        FlashedMessageLevel.MESSAGE: ThemeColor.INFO,
        FlashedMessageLevel.SUCCESS: ThemeColor.SUCCESS,
    }

    ICONS = {
        FlashedMessageLevel.DEBUG: 'fas fa-bug',
        FlashedMessageLevel.ERROR: 'fas fa-ban',
        FlashedMessageLevel.WARNING: 'fas fa-exclamation-triangle',
        FlashedMessageLevel.INFO: 'fas fa-info',
        FlashedMessageLevel.MESSAGE: 'fas fa-info',
        FlashedMessageLevel.SUCCESS: 'fas fa-check',
    }

    __slots__ = ('title', 'text', 'level', '_icon', '_color', 'message_class')

    def __init__(self, title, text, level=FlashedMessageLevel.INFO, icon=None, color=None, message_class=''):
        """
        Arguments:
            title (str): The headline of the message.
            text (str): Message text.
            level (FlashedMessageLevel): The category of the message.
            icon (str): CSS classes for the message icon.
            color (str): Bootstrap CSS class for message color.
            message_class (str): Additional CSS classes.
        """
        self.title = title
        self.text = text
        self.level = level
        self._icon = icon
        self._color = color
        self.message_class = message_class

    @property
    def color(self):
        """Returns the passed color, or the default color for the current category."""
        if self._color is None:
            self._color = self.COLOR.get(self.level)
        return self._color

    @property
    def icon(self):
        """Returns the passed icon, or the default icon for the current category."""
        if self._icon is None:
            self._icon = self.ICONS.get(self.level)
        return self._icon


class MenuItem(object):
    """Application menu item."""

    TYPE_LINK = 'link'
    TYPE_HEADER = 'header'
    TYPE_DROPDOWN_DIVIDER = 'dropdown divider'

    __slots__ = ('_active', '_children', 'id', 'title', 'url', 'parent', 'type', 'icon', 'help', 'badge')

    def __init__(self, id_item, title, url, parent=None,
                 item_type=TYPE_LINK, icon=False, help=None, badge=None):
        """
        Arguments:
            id_item (int|str): the unique identifier of the menu item.
            title (str): item title.
            url (str): the URL that the menu item refers to.
            parent (MenuItem): link to the parent menu item.
            item_type (str): type of menu item, see MenuItem.TYPE_ *.
            icon (str): CSS classes for the icon.
            help (str): hover hint.
            badge (tuple): text label, the first element is text, the second element is style.
        """
        self._active = False
        self._children = []

        self.id = id_item
        self.title = title
        self.url = url
        self.parent = parent
        self.type = item_type
        self.icon = icon
        self.help = help
        self.badge = badge

    def add_badge(self, text, color):
        """Adds a text label to a menu item."""
        self.badge = (text, color)

    def append_child(self, child):
        """Adds a child menu item."""
        child.parent = self
        self._children.append(child)

    @property
    def children(self):
        yield from self._children

    @children.setter
    def children(self, children):
        for child in children:
            self.append_child(child)

    def has_children(self):
        """Returns true if the menu item has a submenu."""
        return bool(self._children)

    def has_parent(self):
        """Returns true if the menu item is a child."""
        return self.parent is not None

    def is_active(self):
        """Returns true if the menu item is selected, otherwise false."""
        return self._active

    def remove_child(self, child):
        # fixme: родитель и исключение
        if child in self.children:
            self._children.remove(child)

    def set_active(self, state):
        """Sets the status of a menu item as active or not."""
        self._active = bool(state)

        if self.has_parent():
            self.parent.set_active(state)


class Menu(object):
    """Application menu."""

    __slots__ = ('_items',)

    def __init__(self):
        self._items = OrderedDict()

    def __iter__(self):
        for id_item, item in self._items.items():
            if not item.has_parent():
                yield item

    def activate_by_path(self, path):
        """Makes active a menu item whose URL matches the one specified in the argument."""
        for item in self._items.values():
            if item.type == MenuItem.TYPE_LINK and item.url == path:
                item.set_active(True)
                return True
        return False

    def add_item(self, item: MenuItem):
        """Adds a new menu item."""
        if item.has_parent():
            item.parent.append_child(item)
        self._items[item.id] = item

    def get_item(self, id_item):
        """Returns a menu item with the specified unique identifier."""
        return self._items.get(id_item)


class Message(DropdownItem):
    """Messages sent to the user."""

    __slots__ = ('sender', 'subject', 'sent_at')

    def __init__(self, sender, subject, url, sent_at=None, icon='fas fa-star', color=ThemeColor.SECONDARY):
        """
        Arguments:
            sender (mixed): the one who sent the message.
            subject (str): message subject.
            url (str): URL to read the message.
            sent_at (datetime): message sending time.
        """
        super().__init__(icon, color)
        self.sender = sender
        self.subject = subject
        self.url = url
        self.sent_at = sent_at or datetime.now()


class Notification(DropdownItem):
    """Notifications sent to the user."""

    __slots__ = ('text', 'sent_at', 'url')

    def __init__(self, text, sent_at=None, url='#', icon=None, color=ThemeColor.GRAY_DARK):
        """
        Arguments:
            text (str): notification text.
            sent_at (datetime): notification sending time.
            url (str): URL to read the notification.
        """
        super().__init__(icon, color)
        self.text = text
        self.sent_at = sent_at or datetime.now()
        self.url = url


class PageItem(object):
    """Page navigation element."""

    __slots__ = ('text', 'url', 'is_active', 'disabled', 'responsive_text')

    def __init__(self, text, url='#', is_active=False, disabled=False, responsive=None):
        self.text = text
        self.url = url
        self.is_active = is_active
        self.disabled = disabled
        self.responsive_text = responsive

    @property
    def responsive(self):
        if not self.responsive_text:
            return self.text
        return self.responsive_text


class Task(DropdownItem):
    """Task in progress."""

    __slots__ = ('title', 'progress', 'url')

    def __init__(self, title, progress, url, icon=None, color=None):
        """
        Arguments:
            title (str): the title of the task to be performed.
            progress (float): progress of the task in percent.
            url (str): URL to show the task.
        """
        super().__init__(icon, color)
        self.title = title
        self.progress = progress
        self.url = url


class User(object):
    """Facade for the original user object."""

    __slots__ = ('_original', '_mapping')

    def __init__(self, original, mapping=None):
        """
        Arguments:
            original (mixed): The original user object.
            mapping (dict): Mapping of properties and methods used in the template
                            to the properties and methods of the original object.
        """
        self._original = original
        self._mapping = mapping or {}

    def __str__(self):
        return str(self._original)

    def _get_attr(self, name, default=None):
        if name in self._mapping:
            name = self._mapping.get(name)

        value = getattr(self._original, name, default)

        if callable(value):
            value = value()

        return value

    __getattr__ = _get_attr

    def get_full_name(self):
        """Returns the full username."""
        return self._get_attr('get_full_name', str(self))
