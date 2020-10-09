"""
Provides functions for creating entities for use with PonyORM.
"""

from pony.orm import Required, Optional, Set, LongStr

from ..data_types import MenuItem
from ..mixins import MenuItemMixin, MenuMixin


__all__ = (
    'create_entity_menu',
    'create_entity_menu_item',
)


def before_insert(self):
    if not (bool(self.url) ^ bool(self.endpoint)):
        raise TypeError('You need to set the value of only one of the arguments: url or endpoint.')


def create_entity_menu_item(db, attributes=None, mixin=None):
    """
    Creates and returns a menu item entity to mapping in the database.

    Arguments:
        db (pony.orm.Database): database instance.
        attributes (dict): entity Attributes.
        mixin (object): mixin with methods for the entity.
    """
    attributes = {
        'menu': Required('Menu'),
        'parent': Optional('MenuItem', reverse='items'),
        'items': Set('MenuItem', reverse='parent'),
        'type': Required(str, 20, default=MenuItem.TYPE_LINK),
        'title': Required(str, 500),
        'url': Optional(str, 500),
        'endpoint': Optional(str, 255),
        'endpoint_args': Optional(LongStr),
        'endpoint_kwargs': Optional(LongStr),
        'icon': Optional(str, 50),
        'help': Optional(str, 500),
        'pos': Optional(int, default=0),
        'before_insert': before_insert,
        **(attributes or {}),
    }

    if mixin is None:
        base = (db.Entity, MenuItemMixin)
    else:
        base = (db.Entity, mixin, MenuItemMixin)

    return type('MenuItem', base, attributes)


def create_entity_menu(db, attributes=None, mixin=None):
    """
    Creates and returns a menu entity to mapping in the database.

    Arguments:
        db (pony.orm.Database): database instance.
        attributes (dict): entity Attributes.
        mixin (object): mixin with methods for the entity.
    """
    attributes = {
        'title': Required(str, 500),
        'program_name': Required(str, unique=True, index=True),
        'items': Set('MenuItem'),
        **(attributes or {})
    }

    if mixin is None:
        base = (db.Entity, MenuMixin)
    else:
        base = (db.Entity, mixin, MenuMixin)

    return type('Menu', base, attributes)
