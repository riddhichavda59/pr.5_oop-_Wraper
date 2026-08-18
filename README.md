# 👨‍💼 Employee Management System

A **Python-based Employee Management System** developed using **Object-Oriented Programming (OOP)** concepts. This project is designed to demonstrate how OOP principles can be applied to build a simple, practical, and menu-driven real-world application.

---

## 📌 Project Overview

The **Employee Management System** allows users to create, manage, search, update, display, and delete employee information through a simple command-line interface.

The project uses different classes and inheritance relationships to represent different types of employees such as:

* Employee
* Manager
* Developer

The main purpose of this project is to understand and practically implement important **Python OOP concepts**.

---

## 🎯 Project Objective

The main objectives of this project are:

* To understand the fundamentals of Object-Oriented Programming.
* To implement classes and objects in Python.
* To understand inheritance and method overriding.
* To implement encapsulation using private attributes.
* To use constructors and destructors.
* To understand the use of `super()`.
* To implement getter and setter methods.
* To understand method overloading-like behavior in Python.
* To use `issubclass()` for checking inheritance.
* To build a simple real-world application using OOP.

---

## ✨ Features

The system provides the following features:

* ✅ Create Employee
* ✅ Create Manager
* ✅ Create Developer
* ✅ Display all employee details
* ✅ Search employee by Employee ID
* ✅ Update employee salary
* ✅ Delete employee
* ✅ Manage employee information
* ✅ Menu-driven command-line interface
* ✅ Demonstration of OOP concepts
* ✅ Employee ID uniqueness validation
* ✅ Basic input validation

---

## 🏗️ Class Structure

The project follows the following inheritance hierarchy:

```text
                    Person
                       │
                       ▼
                   Employee
                  /        \
                 /          \
                ▼            ▼
            Manager       Developer
```

### Person

The `Person` class is the base class.

It contains:

* Name
* Age

It also provides getter and setter methods for managing personal information.

---

### Employee

The `Employee` class inherits from `Person`.

It contains:

* Employee ID
* Name
* Age
* Salary

The class also provides:

* Getter and setter methods
* Salary update functionality
* Employee detail display
* Constructor
* Destructor

---

### Manager

The `Manager` class inherits from `Employee`.

In addition to employee information, it contains:

* Department

The `Manager` class overrides the `display_details()` method to display manager-specific information.

---

### Developer

The `Developer` class inherits from `Employee`.

In addition to employee information, it contains:

* Programming Language

The `Developer` class overrides the `display_details()` method to display developer-specific information.

---

## 🧠 OOP Concepts Used

### 1. Class and Object

Classes are used to define the structure and behavior of the application.

Objects are created from these classes to store and manage employee data.

Example:

```python
employee = Employee("E101", "Rahul", 25, 50000)
```

---

### 2. Inheritance

Inheritance allows one class to acquire the properties and methods of another class.

In this project:

```text
Person → Employee → Manager
                     ↘ Developer
```

For example:

```python
class Manager(Employee):
    pass
```

The `Manager` class inherits the features of the `Employee` class.

---

### 3. Encapsulation

Encapsulation is implemented using private attributes.

Private attributes are represented using double underscores:

```python
self.__salary
self.__employee_id
```

These attributes are accessed and modified using getter and setter methods.

---

### 4. Constructor

The constructor is implemented using the `__init__()` method.

It is automatically called when an object is created.

Example:

```python
def __init__(self, employee_id, name, age, salary):
    self.__employee_id = employee_id
    self.__salary = salary
```

---

### 5. Destructor

The destructor is implemented using the `__del__()` method.

It is called when an object is being destroyed.

Example:

```python
def __del__(self):
    print("Object deleted.")
```

---

### 6. Method Overriding

Child classes provide their own implementation of a method inherited from the parent class.

In this project, both `Manager` and `Developer` override:

```python
display_details()
```

This allows each class to display its own specific information.

---

### 7. Method Overloading

Python does not support traditional method overloading in the same way as languages such as Java or C++.

Therefore, this project demonstrates **overloading-like behavior using default arguments**.

Example:

```python
def update_salary(self, new_salary, bonus=0):
    self.__salary = new_salary + bonus
```

The method can be called with either one or two arguments.

---

### 8. `super()`

The `super()` function is used to access the constructor or methods of the parent class.

Example:

```python
super().__init__(name, age)
```

This allows the child class to reuse the functionality of its parent class.

---

### 9. Getter and Setter

Getter methods are used to retrieve private data.

Setter methods are used to update private data safely.

Example:

```python
def get_salary(self):
    return self.__salary

def set_salary(self, salary):
    self.__salary = salary
```

This helps implement encapsulation.

---

### 10. `issubclass()`

The `issubclass()` function is used to check whether one class is derived from another class.

Example:

```python
issubclass(Manager, Employee)
```

Output:

```text
True
```

---

## 📋 Menu

The application provides the following menu:

```text
=======================================================
        EMPLOYEE MANAGEMENT SYSTEM
=======================================================
1. Create Employee
2. Create Manager
3. Create Developer
4. Show All Employees
5. Search Employee
6. Update Salary
7. Delete Employee
8. Show OOP Concepts
9. Exit
=======================================================
```

---

## 🔄 How the System Works

### Step 1 — Start the Program

Run the Python program from the terminal.

### Step 2 — Select an Option

The user selects an option from the main menu.

### Step 3 — Enter Information

Depending on the selected option, the user enters employee information such as:

* Employee ID
* Name
* Age
* Salary
* Department
* Programming Language

### Step 4 — Manage Employees

The system stores employee objects and allows the user to:

* View employees
* Search employees
* Update salary
* Delete employees

### Step 5 — Exit

The user can select the **Exit** option to terminate the program.

---

## 💻 Technologies Used

| Technology             | Purpose                  |
| ---------------------- | ------------------------ |
| Python                 | Programming Language     |
| OOP                    | Application Design       |
| Command Line Interface | User Interaction         |
| Dictionary             | Employee Data Management |

---

## 📁 Project Structure

```text
Employee-Management-System/
│
├── employee_management.py
│
└── README.md
```

---

## ⚙️ Requirements

Before running the project, make sure Python is installed on your computer.

Check the Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

The project does not require any external Python libraries.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd Employee-Management-System
```

### 3. Run the program

```bash
python employee_management.py
```

---

## 🖥️ Sample Output

### Creating a Manager

```text
========== Create Manager ==========

Enter Employee ID: M101
Enter Name: Rahul
Enter Age: 35
Enter Salary: 75000
Enter Department: IT

Manager created successfully!
```

### Displaying Employee Details

```text
-----------------------------------
Manager Details
-----------------------------------
Employee ID : M101
Name        : Rahul
Age         : 35
Salary      : ₹75000.00
Department  : IT
Type        : Manager
-----------------------------------
```

---

## 🔐 Data Validation

The application performs basic validation such as:

* Employee ID must be unique.
* Age must be greater than zero.
* Salary cannot be negative.
* Name cannot be empty.
* Department cannot be empty.
* Programming language cannot be empty.
* Invalid numeric input is handled.

---

## 📚 Learning Outcomes

After completing this project, you will understand:

* How to create classes and objects in Python.
* How inheritance works.
* How to implement encapsulation.
* How constructors and destructors work.
* How method overriding works.
* How Python handles overloading-like behavior.
* How to use `super()`.
* How getter and setter methods work.
* How `issubclass()` works.
* How OOP can be used to solve real-world problems.
* How to create a menu-driven Python application.

---

## 🚀 Future Improvements

The project can be further enhanced by adding:

* 🔹 File handling for permanent data storage
* 🔹 SQLite/MySQL database integration
* 🔹 Employee attendance management
* 🔹 Employee leave management
* 🔹 Department-wise employee search
* 🔹 Employee performance management
* 🔹 Login and authentication system
* 🔹 GUI using Tkinter
* 🔹 Web application using Flask or Django
* 🔹 Export employee data to CSV/Excel

---

## ⚠️ Note About Method Overloading

Python does not provide traditional method overloading based solely on different parameter lists.

For example, Python does not support defining:

```python
method(a)
method(a, b)
```

as two separate methods in the same class.

Instead, this project uses **default parameters** to demonstrate similar behavior:

```python
def update_salary(self, new_salary, bonus=0):
    self.__salary = new_salary + bonus
```

This is an important concept to understand when explaining the project during a viva.

---

## 👨‍💻 Author

**Your Name**

> Python OOP Project — Employee Management System

---

## 📄 License

This project is created for **educational and learning purposes**.

You are free to modify and improve the project for your own learning and academic use.

---

## ⭐ Conclusion

The **Employee Management System** is a simple Python application developed to demonstrate the practical implementation of Object-Oriented Programming concepts.

By using classes such as `Person`, `Employee`, `Manager`, and `Developer`, the project demonstrates how inheritance, encapsulation, constructors, destructors, method overriding, getters, setters, and `super()` can be combined to create a structured real-world application.

This project provides a strong foundation for learning Python OOP and can be extended into a more advanced employee management application using databases, GUI frameworks, or web technologies.


# Video Explanation:
