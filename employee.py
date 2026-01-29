
class Employee:
    
    num_of_emps = 0
    raise_amount = 1.05
    
    def __init__(self, firstname: str, lastname: str, id: int, pay: float) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.pay = pay
        
        Employee.num_of_emps += 1
        
    def __repr__(self):
        return f'Employee(Name: {self.firstname} {self.lastname}, Id: {self.id}, Pay: {self.pay})'
    
    def __str__(self):
        return f'Employee Instance\n\tGiven Name\t: {self.firstname}\n\tLast Name\t: {self.lastname}\n\tId\t\t: {self.id}\n\tPay Amount\t: {self.pay}'
    
    def add(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay
        raise TypeError('Other is not an instance of Employee class.') 
        
    def payDiff(self, other):
        if isinstance(other, Employee):
            return self.pay - other.pay
        raise TypeError('Other is not an instance of Employee class.')
    
    def get_email(self):
        return f'{self.firstname}.{self.lastname}@company.com'
    
    def apply_raise(self):
        self.pay *= Employee.raise_amount 
