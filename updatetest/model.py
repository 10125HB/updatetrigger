"""A simple model class with a decorator to call the update method after a method."""
import logging


logger = logging.getLogger()


def call_update_after(method):
    """Decorator to call the update method after a method."""
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if not self.prevent_update:
            self.update()
        return result
    return wrapper


class Model:
    """A simple model class."""
    def __init__(self):
        self._a: float = 1.0
        self._b: float = 2.0
        self._value = 0
        self.prevent_update = False
        logger.info("Model created. Parameters: a=%s, b=%s, value=%s", self._a, self._b, self._value)

    def update(self):
        """Update the value of the model."""
        self._value += self._a + self._b
        logger.info("Updated. Parameters: a=%s, b=%s, value=%s", self._a, self._b, self._value)

    @property
    def a(self):
        """The value of a."""
        return self._a

    @a.setter
    @call_update_after
    def a(self, value):
        self._a = value
        logger.info("Set a to %s", value)

    @property
    def b(self):
        """The value of b"""
        return self._b

    @b.setter
    @call_update_after
    def b(self, value):
        self._b = value
        logger.info("Set b to %s", value)
