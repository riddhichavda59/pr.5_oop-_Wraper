# Python OOP Project:

print("------Python OOP Projec: Employee Management System ------")

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print("Name:",self.name)
        print("Age:",self.age)

class Employee:

    def __init__(self,name=None,age=None,employee_id=None,salary=None):

        self.name = name
        self.age = age
        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id 

    def set_id(self,employee_id):

        if self.__employee_id > 0:

            self.__employee_id = empolyee_id

        else:

            print("Invalid EmployeeId.")


    # salary

    def get_salary(self):

        return self.__salary
    
    def set_salary(self,salary):

        if salary > 0:
            self.__salary = salary

        else:
            print("Invalid salary")
    

    def display(self):
        print(f"Employee created with name:,{self.name},age:,{self.age},employee:,{self.get_employee_id},salary:,{self.get_salary}.")
    def e_display(slf):

        super().person_display()

        print("Employee_Id:",self.get_employee_id)

        print("salary:",self.get_salary)
        
                        
class Manager(Employee):
    def __init__(self,name,age,employee_id,salary,department):
        
         super().__init__(name,age,employee_id,salary)
         self.department = department

    def display(self):

        super().display()

        print(f"Manager created with name:{self.name},age:{self.age},employee_id:{self.get_employee_id},salary:{self.get_salary}and department:{self.department}")

        
class Developer(Employee):

    def __init__(self,name,age,employee_id,salary,department,language):

        super().__init_(name,age,employee_id,salary,department)

        set.language = language

    def developer_display(self):

        print(f"Dvloper created with name:{self.name},age:{self.age},employee_id:{self.get_empolyee_id},salary:{self.get_salary}and department:{self.department},and language:{self.language}.")
    def developer_display(self):

        super().manager_display()

        print("Language:",self.language)

while True:
    print("\n----choose an Operation----")
    print("1.Create a Person")
    print("2.Create an Employee")
    print("3.Create a Manager")
    print("4.Create a Developer")
    print("5.Show Details")
    print("6.Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        person = Person(name, age)
        print("\nPerson created successfully!")

    elif choice == "2":

        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        emp_id = input("Enter Employee ID : ")
        salary = float(input("Enter Salary : "))

        employee = Employee(name,age,emp_id,salary)

        print("\nEmployee created successfully!")

    elif choice == "3":

        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        emp_id = input("Enter Employee ID : ")
        salary = float(input("Enter Salary : "))
        department = input("Enter Department : ")

        manager = Manager(name,age,emp_id,salary,department)

        print("\nManager created successfully!")

    elif choice =="4":
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        emp_id = input("Enter Employee ID : ")
        salary = float(input("Enter Salary : "))
        department = input("Enter Department : ")
        language = input("Enter Language:")


    elif choice == "5":

        print("\n1. Person")
        print("2. Employee")
        print("3. Manager")

        option = input("Choose details to show : ")
        if option == "1":

            if person is not None:
                person.display()
            else:
                print("No Person data found!")

        elif option == "2":

            if employee is not None:
                employee.display()
            else:
                print("No Employee data found!")

        elif option == "3":

            if manager is not None:
                manager.display()
            else:
                print("No Manager data found!")
        else:
            print("Invalid Choice!")

    elif choice == "6":

        print("\nExiting the system. Goodbye!")
        break
        
    else:
        print("Invalid choice! Try again.")



    
