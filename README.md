# Copy-on-Write (CoW) Python Library

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

## 🚀 Introduction
**Copy-on-Write (CoW)** is a memory optimization technique that delays copying objects **until they are modified**. This Python library provides a seamless CoW wrapper for **lists, dictionaries, sets, and strings**, ensuring **efficient memory usage** while maintaining **native Python APIs**.

## 🔧 Features
- ✅ **Supports lists, dicts, sets, and strings**
- ✅ **Lazy copying** - modifications trigger copying, reads do not
- ✅ **Seamless API** - use `.append()`, `.update()`, etc. as usual
- ✅ **Optimized performance & memory efficiency**
- ✅ **Fully tested with `unittest`**
- ✅ **Python 3.6+ compatible**

---

## 📦 Installation
### **Install via pip (Coming Soon on PyPI)**
```sh
pip install copyonwrite
```
or install manually:
```sh
git clone https://github.com/yourusername/copyonwrite.git
cd copyonwrite
pip install .
```

---

## 🚀 Usage Examples

### **✅ Copy-on-Write List**
```python
from copyonwrite import cow

l = [1, 2, 3, 4]
cow_list = cow(l)

cow_list.append(5)  # Triggers Copy-on-Write
print(cow_list)  # Output: [1, 2, 3, 4, 5]
print(l)  # Output: [1, 2, 3, 4] (Original remains unchanged)
```

### **✅ Copy-on-Write Dictionary**
```python
d = {"a": 1, "b": 2}
cow_dict = cow(d)

cow_dict["a"] = 42  # Triggers Copy-on-Write
print(cow_dict)  # Output: {'a': 42, 'b': 2}
print(d)  # Output: {'a': 1, 'b': 2} (Original remains unchanged)
```

### **✅ Copy-on-Write Set**
```python
s = {1, 2, 3}
cow_set = cow(s)

cow_set.add(4)  # Triggers Copy-on-Write
print(cow_set)  # Output: {1, 2, 3, 4}
print(s)  # Output: {1, 2, 3} (Original remains unchanged)
```

### **✅ Copy-on-Write String**
```python
string = "hello"
cow_string = cow(string)

print(cow_string.upper())  # Output: "HELLO"
print(cow_string)  # Output: "hello" (Original remains unchanged)
```

---

## 🛠 API Reference
### **`cow(data: Any) -> Cow`**
Creates a **Copy-on-Write wrapper** around the given `list`, `dict`, `set`, or `str`.

#### ✅ **Supported Methods**
| **Type** | **Supported Methods** |
|----------|-----------------------|
| **List** | `append()`, `extend()`, `__getitem__()`, `__setitem__()` |
| **Dict** | `update()`, `pop()`, `clear()`, `__getitem__()`, `__setitem__()` |
| **Set**  | `add()`, `remove()`, `discard()`, `clear()` |
| **String** | Read-only operations (`upper()`, `replace()`, slicing) |

---

## 🧪 Running Tests
The library is fully tested with `unittest`. Run the test suite using:

```sh
python -m unittest discover tests
```

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. **Fork the repository**
2. **Create a feature branch**
3. **Write tests for your changes**
4. **Submit a pull request**

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 🌟 Support
If you find this project useful, **consider giving it a star ⭐ on GitHub!**
