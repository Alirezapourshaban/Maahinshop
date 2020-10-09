"""
Mixins to create your own entity classes.
"""

__all__ = (
    'MenuItemMixin', 'MenuMixin',
)


class MenuItemMixin(object):
    """Mixin for the database model, which describes the menu item."""

    def get_endpoint(self):
        """Returns the name of the entry point / route."""
        return self.endpoint

    def get_endpoint_args(self):
        """Returns the nameless arguments to the route."""
        return self.endpoint_args.split()

    def get_endpoint_kwargs(self):
        """Returns the named arguments to the route."""
        return dict(p.split('=') for p in self.endpoint_kwargs.splitlines())

    def get_hint(self):
        """Returns a hint to the user."""
        return self.help

    def get_icon(self):
        """Returns the css class of the icon."""
        return self.icon

    def get_id(self):
        """Returns a unique identifier for a menu item."""
        return self.id

    def get_parent_id(self):
        """Returns the unique identifier of the parent menu item."""
        return self.parent and self.parent.get_id()

    def get_pos(self):
        """Returns the position of an item in a menu."""
        return self.pos

    def get_title(self):
        """Returns the title of a menu item."""
        return self.title

    def get_type(self):
        """Returns the type of menu item."""
        return self.type

    def get_url(self):
        """Returns the URL that this menu item refers to."""
        return self.url


class MenuMixin(object):
    """Mixin for the database model that describes the menu."""

    def get_items(self):
        """Returns menu items strictly sorted in ascending order by parent and position."""
        return self.items

    def get_program_name(self):
        """Returns a unique menu name to display on the page."""
        return self.program_name

    def get_title(self):
        """Returns the title of the menu."""
        return self.title
