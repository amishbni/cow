from copy import deepcopy

from typing import Any, Optional

class Cow:
    """A generic Copy-on-Write wrapper for mutable data structures."""

    def __init__(self, data: Any) -> None:
        object.__setattr__(self, "_shared_data", data)
        object.__setattr__(self, "_private_data", None)

    def _copy_on_write(self) -> None:
        if self._private_data is None:
            object.__setattr__(self, "_private_data", deepcopy(self._shared_data))

    @property
    def data(self) -> Any:
        if self._private_data is not None:
            return self._private_data
        return self._shared_data

    def __add__(self, other: Any) -> "Cow":
        return self.data + (other.data if isinstance(other, Cow) else other)

    def __getattr__(self, item):
        return getattr(self.data, item)

    def __setattr__(self, key, value):
        self._copy_on_write()
        setattr(self.data, key, value)

    def __delattr__(self, item):
        self._copy_on_write()
        delattr(self.data, item)

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self._copy_on_write()
        self.data[key] = value

    def __delitem__(self, key):
        self._copy_on_write()
        del self.data[key]

    def __repr__(self):
        return repr(self.data)

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

    def __eq__(self, other):
        return self.data == (other.data if isinstance(other, Cow) else other)

    def append(self, value):
        self._copy_on_write()
        self.data.append(value)

    def extend(self, values):
        self._copy_on_write()
        self.data.extend(values)

    def add(self, value):
        self._copy_on_write()
        self.data.add(value)

    def remove(self, value):
        self._copy_on_write()
        self.data.remove(value)

    def discard(self, value) -> None:
        self._copy_on_write()
        self.data.discard(value)

    def clear(self):
        self._copy_on_write()
        self.data.clear()

    def pop(self, index: Optional[Any] = None, default: Optional[Any] = None) -> Any:
        self._copy_on_write()
        if isinstance(self.data, set):
            if index is not None or default is not None:
                raise TypeError("set.pop() takes no arguments.")
            return self.data.pop()
        return self.data.pop(index, default)

    def popitem(self):
        self._copy_on_write()
        return self.data.popitem()

    def update(self, values):
        self._copy_on_write()
        self.data.update(values)


def cow(data: Any) -> Cow:
    if isinstance(data, (list, dict, set, str)):
        return Cow(data)
    raise TypeError("CoW only supports lists, dicts, sets and strings.")
