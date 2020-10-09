from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr

from ..data_types import MenuItem
from ..mixins import MenuItemMixin as _MenuItemMixin, MenuMixin as _MenuMixin


__all__ = (
    'MenuItemMixin', 'create_entity_menu_item',
)


class MenuItemMixin(_MenuItemMixin):
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key=True)

    @declared_attr
    def menu_id(cls):
        return Column(ForeignKey('menu.id'), nullable=False)

    @declared_attr
    def parent_id(cls):
        return Column(ForeignKey('menu_item.id'))

    @declared_attr
    def parent(cls):
        return relationship('MenuItem', remote_side=[cls.id])

    type = Column(String(20), default=MenuItem.TYPE_LINK, nullable=False)
    title = Column(String(500), nullable=False)
    url = Column(Text, default='', nullable=False)
    endpoint = Column(String(255), default='', nullable=False)
    endpoint_args = Column(Text, default='', nullable=False)
    endpoint_kwargs = Column(Text, default='', nullable=False)
    icon = Column(String(50), default='', nullable=False)
    help = Column(String(500), default='', nullable=False)
    pos = Column(Integer, default=0, nullable=False)


class MenuMixin(_MenuMixin):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False)
    program_name = Column(String(255), unique=True, index=True, nullable=False)

    @declared_attr
    def items(cls):
        return relationship('MenuItem', backref='menu', lazy='joined')


def create_entity_menu_item(db):
    return type('MenuItem', (db.Model, MenuItemMixin), {})


def create_entity_menu(db):
    return type('Menu', (db.Model, MenuMixin), {})
