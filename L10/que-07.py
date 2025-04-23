# Program que-07.py
# Serialize and deserialize an Employee object with empcode, empname, Date of Joining, Salary

import pickle
from datetime import datetime

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj  # Date of Joining as datetime object
        self.salary = salary

    def __str__(self):
        return f"Employee[empcode={self.empcode}, empname={self.empname}, doj={self.doj.strftime('%Y-%m-%d')}, salary={self.salary}]"

def serialize_employee(emp, filename):
    with open(filename, 'wb') as f:
        pickle.dump(emp, f)
    print(f"Serialized employee data to {filename}")

def deserialize_employee(filename):
    with open(filename, 'rb') as f:
        emp = pickle.load(f)
    print(f"Deserialized employee data from {filename}")
    return emp

emp = Employee(empcode=101, empname="John Doe", doj=datetime(2020, 5, 15), salary=75000)
filename = "que-07-employee.dat"
serialize_employee(emp, filename)
emp_loaded = deserialize_employee(filename)
print(emp_loaded)
