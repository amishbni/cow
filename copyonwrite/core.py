from copy import deepcopy

from typing import Any

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
        if not isinstance(self.data, list):
            raise TypeError("append() is only supported for lists.")
        self._copy_on_write()
        self.data.append(value)

    def extend(self, values):
        if not isinstance(self.data, list):
            raise TypeError("extend() is only supported for lists.")
        self._copy_on_write()
        self.data.extend(values)

    def add(self, value):
        if not isinstance(self.data, set):
            raise TypeError("add() is only supported for sets.")
        self._copy_on_write()
        self.data.add(value)

    def clear(self):
        if not isinstance(self.data, dict):
            raise TypeError("clear() is only supported for dicts.")
        self._copy_on_write()
        self.data.clear()

    def pop(self, value):
        if not isinstance(self.data, dict):
            raise TypeError("pop() is only supported for dicts.")
        self._copy_on_write()
        return self.data.pop(value)

    def popitem(self):
        if not isinstance(self.data, dict):
            raise TypeError("popitem() is only supported for dicts.")
        self._copy_on_write()
        return self.data.popitem()

    def update(self, values):
        if not isinstance(self.data, dict):
            raise TypeError("update() is only supported for dicts.")
        self._copy_on_write()
        self.data.update(values)


def cow(data: Any) -> Cow:
    if isinstance(data, (list, dict, set, str)):
        return Cow(data)
    raise TypeError("CoW only supports lists, dicts, sets and strings.")
