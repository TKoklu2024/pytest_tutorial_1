from employee import Employee
import pytest

def test_verify_that_employee_email_is_set_automatically():
    emp = Employee('Test', 'User', 1001, 55_000)
    assert emp.get_email() == 'Test.User@company.com'
    
def test_verify_that_adding_two_employees_payamount():
    emp1 = Employee('Test1', 'User1', 1001, 55_000)
    emp2 = Employee('Test2', 'User2', 1002, 40_000)
    assert emp1.add(emp2) == 95_000
    
def test_verify_that_TypeError_is_raised_when_an_instance_is_not_Employee():
    emp = Employee('Test', 'User', 1002, 60_000)
    other = 'Employee instance'
    with pytest.raises(TypeError):
        emp.add(other=other)
        
def test_verify_that_difference_between_two_employees_payamount():
    emp1 = Employee('Test1', 'User1', 1001, 55_000)
    emp2 = Employee('Test2', 'User2', 1002, 40_000)
    assert emp1.payDiff(emp2) == 15_000
    
def test_verify_that_the_number_of_employees_created():
    emp1 = Employee('Test1', 'User1', 1001, 55_000)
    emp2 = Employee('Test2', 'User2', 1002, 55_000)
    emp3 = Employee('Test3', 'User3', 1003, 55_000)
    assert Employee.num_of_emps != 0