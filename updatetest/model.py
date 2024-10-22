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

    def update(self):
        """Update the value of the model."""
        self._value += self._a + self._b
        print(f"Value: {self._value}")

    @property
    def a(self):
        """The value of a."""
        return self._a

    @a.setter
    @call_update_after
    def a(self, value):
        self._a = value
