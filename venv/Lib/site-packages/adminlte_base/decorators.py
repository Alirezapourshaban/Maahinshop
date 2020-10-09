from functools import wraps
from collections import namedtuple


__all__ = ('return_namedtuple',)


def return_namedtuple(name, *fields):
    defaults = (None,) * len(fields)
    Result = namedtuple(name, fields, defaults=defaults)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if isinstance(result, tuple):
                return Result(*result)

            return result

        return wrapper

    return decorator
