import time
from employee import Employee
import pytest

@pytest.mark.slow
def test_verify_that_employee_email_is_set_automatically():
    emp = Employee('Test', 'User', 1001, 55_000)
    assert emp.get_email() == 'Test.User@company.com'

@pytest.mark.fast    
def test_verify_that_adding_two_employees_payamount():
    emp1 = Employee('Test1', 'User1', 1001, 55_000)
    emp2 = Employee('Test2', 'User2', 1002, 40_000)
    # time.sleep(2)  # Uncomment this to see simulation of a slow test results
    assert emp1.add(emp2) == 95_000, f'Expected pay amount to be 95_000 but got {emp1.add(emp2)}'

@pytest.mark.regression    
def test_verify_that_TypeError_is_raised_when_an_instance_is_not_Employee():
    emp = Employee('Test', 'User', 1002, 60_000)
    other = 'Employee instance'
    with pytest.raises(TypeError):
        emp.add(other=other)

@pytest.mark.smoke        
def test_verify_that_difference_between_two_employees_payamount():
    emp1 = Employee('Test1', 'User1', 1001, 55_000)
    emp2 = Employee('Test2', 'User2', 1002, 40_000)
    assert emp1.payDiff(emp2) == 15_000

@pytest.mark.integration
def test_verify_that_the_number_of_employees_created():
    emp1 = Employee('Test1', 'User1', 1001, 55_000)
    emp2 = Employee('Test2', 'User2', 1002, 55_000)
    emp3 = Employee('Test3', 'User3', 1003, 55_000)
    assert Employee.num_of_emps != 0
    
def test_verify_that_custom_assertion_representation_works_correctly():
    emp1 = Employee('Test1', 'User1', 1001, 60_000)
    emp2 = Employee('Test2', 'User2', 1002, 60_000)
    assert emp1 == emp2
