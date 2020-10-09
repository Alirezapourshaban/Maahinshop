__all__ = (
    'Error', 'MenuNotFound'
)


class Error(Exception):
    """The base type for all exceptions thrown in the library."""


class MenuNotFound(Error, ValueError):
    """An exception is thrown when a menu with the passed name is not found."""

    def __init__(self, program_name):
        self.program_name = program_name
        super().__init__(f'The menu with the program name "{program_name}" cannot be loaded.')
