# 🐍 Python Object-Oriented Programming (OOP)

> **A structured and comprehensive guide to Python's Object-Oriented paradigm, covering Classes, Encapsulation, Inheritance Hierarchies, Polymorphism, Operator Overloading, and Abstract Base Classes (ABCs).**

---

## 📌 Repository Overview

This repository provides clear, practical Python implementations demonstrating the core architectural pillars of Object-Oriented Programming (OOP). Unlike conventional syntax-only references, each module illustrates Python-specific mechanics including __init__ constructor semantics, name mangling, multiple inheritance with Method Resolution Order (MRO), dunder/magic methods, and formal interface enforcement using the bc module.

---

## 🗂️ Curriculum & Directory Structure

`	ext
python-oops/
├── class_object/
│   ├── class_basics.py             # Class definitions, state vs behavior, instance attributes
│   ├── constructor_example.py      # __init__ lifecycle, parameter passing & default arguments
│   └── object_creation.py          # Instantiation, identity comparison (is vs ==) & namespaces
├── encapsulation/
│   ├── public_members.py           # Unrestricted attribute access and standard convention
│   ├── protected_members.py        # Single underscore convention (_member) for subclass access
│   └── private_members.py          # Double underscore (__member) name-mangling in Python
├── inheritance/
│   ├── single_inheritance.py       # Base class to derived class with super() invocation
│   ├── multiple_inheritance.py     # Inheriting from multiple parents & C3 linearization (MRO)
│   ├── multilevel_inheritance.py   # Grandparent -> Parent -> Child inheritance chains
│   └── hierarchical_inheritance.py # Single parent specialized by multiple distinct subclasses
├── polymorphism/
│   ├── polymorphism_example.py     # Duck typing and uniform interface processing
│   ├── method_overriding.py        # Dynamic dispatch and overriding parent methods
│   └── operator_overloading.py     # Magic/Dunder methods (__add__, __str__, __len__)
└── abstraction/
    ├── abstract_class.py           # abc.ABC, @abstractmethod, and incomplete class constraints
    └── interface_example.py        # Pure abstract interfaces enforcing API contracts
`

---

## 🔬 Core OOP Pillars Explained

### 1. Classes & Constructors (class_object/)
- Demonstrates defining custom types, binding instance methods via self, and initialization lifecycle hooks.

### 2. Encapsulation & Data Hiding (encapsulation/)
- Explains Python's attribute visibility philosophy:
  - **Public**: ttribute
  - **Protected (convention)**: _attribute (signals internal use to fellow developers)
  - **Private (name mangling)**: __attribute (mangled to _ClassName__attribute to prevent accidental collision)

### 3. Inheritance & Reusability (inheritance/)
- Explores code specialization across single, multiple, multilevel, and hierarchical structures.
- Highlights cooperative multiple inheritance using super() and inspects Class.__mro__.

### 4. Polymorphism & Dunder Methods (polymorphism/)
- Emphasizes Python's "duck typing" philosophy (*if it walks and quacks like a duck, it is a duck*).
- Implements operator overloading by binding Python operators (+, -, etc.) to custom class logic using special dunder methods.

### 5. Abstraction & Interfaces (bstraction/)
- Enforces strict design contracts using Python's standard bc (Abstract Base Classes) library.
- Demonstrates preventing direct instantiation of abstract classes and guaranteeing subclasses implement required abstract methods.

---

## 🚀 Running the Examples

All examples are standalone Python scripts requiring standard Python 3.8+:

`ash
# Example: Run constructor demonstration
python class_object/constructor_example.py

# Example: Run multiple inheritance & MRO
python inheritance/multiple_inheritance.py

# Example: Run operator overloading
python polymorphism/operator_overloading.py

# Example: Run abstract classes
python abstraction/abstract_class.py
`

---

## 📄 License

This repository is distributed under the [MIT License](LICENSE).

---

## 👩‍💻 Author

**Simran Gupta**
- GitHub: [@Simranroshangupta](https://github.com/Simranroshangupta)
