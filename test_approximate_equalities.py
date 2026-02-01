import time
from employee import Employee
import pytest
import numpy as np

def test_verifty_that_employee_payamouts_are_approximately_equal():
    emp1 = Employee('Test1', 'User1', 1001, 55000.1234)
    emp2 = Employee('Test2', 'User2', 1002, 55000.1239)
    assert pytest.approx(emp1.pay, abs=0.001) == emp2.pay
    
def test_verifty_that_employee_payamouts_are_not_approximately_equal():
    emp1 = Employee('Test1', 'User1', 1001, 55000.123)
    emp2 = Employee('Test2', 'User2', 1002, 55000.124)
    assert pytest.approx(emp1.pay, abs=0.001) != emp2.pay
    
def test_verifty_that_employee_payamouts_are_approximately_equal_relative():
    emp1 = Employee('Test1', 'User1', 1001, 55000)
    emp2 = Employee('Test2', 'User2', 1002, 55055)
    assert pytest.approx(emp1.pay, rel=0.001) == emp2.pay
    
def test_verifty_that_employee_payamouts_are_approximately_equal_with_numpy_array_usage():
    emp1 = Employee('Test1', 'User1', 1001, 55000.1234)
    emp2 = Employee('Test2', 'User2', 1002, 55000.1235)
    emp3 = Employee('Test3', 'User3', 1003, 55000.1236)
    emp4 = Employee('Test4', 'User4', 1004, 55000.1237)
    a = np.array([emp1.pay, emp2.pay])
    b = np.array([emp3.pay, emp4.pay])
    assert pytest.approx(a, abs=0.001) == b