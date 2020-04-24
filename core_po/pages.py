import abc
import attr
import typing

from core_po.mixins import ResponseShortcutsMixin
from core_po.page_inputs import ResponseData


class Injectable(abc.ABC):
    """Injectable objects are automatically built and passed as arguments to
    callbacks that requires them.

    Instead of inheriting you can also use ``Injectable.register(MyWebPage)``.
    ``Injectable.register`` can also be used as a decorator.
    """
    pass


# NoneType is considered as injectable. Required for Optionals to work.
Injectable.register(type(None))


def is_injectable(obj: typing.Any) -> bool:
    """Checks if an object inherits from ``Injectable``."""
    return isinstance(obj, type) and issubclass(obj, Injectable)


class ItemPage(Injectable, abc.ABC):
    """Describes the base Page Object.

     Page Objects require the ``to_item`` method to be implemented in order
     to expose acquired data.
     """

    @abc.abstractmethod
    def to_item(self):
        """Exposes Page Object's data."""
        pass


@attr.s(auto_attribs=True)
class WebPage(Injectable, ResponseShortcutsMixin):
    """Describes the base Web Page Object.

    It's a Page Object that depends on basic response data to provide XPath
    and CSS shortcuts.

    This class should be used as a base for other Web Page Objects.
    """
    response: ResponseData


@attr.s(auto_attribs=True)
class ItemWebPage(WebPage, ItemPage):
    """
    ``WebPage`` that implements the ``to_item`` method.
    """
    pass
