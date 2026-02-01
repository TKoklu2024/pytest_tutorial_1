import pytest
from employee import Employee


def test_verify_that_an_none_implementation_error_is_raised():
    emp = Employee('Test', 'User', 1001, 55_000)
    with pytest.raises(NotImplementedError):
        emp.raises_a_NoneImplementation()
        
def test_verify_that_type_error_is_raised_when_adding_non_employee_instance():
    emp = Employee('Test', 'User', 1002, 60_000)
    other = 'Employee instance'
    with pytest.raises(TypeError):
        emp.add(other=other)
        
def test_verify_that_type_error_is_raised_when_calculating_paydiff_with_non_employee_instance():
    emp = Employee('Test', 'User', 1003, 70_000)
    other = 50000
    with pytest.raises(TypeError):
        emp.payDiff(other=other)