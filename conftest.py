from employee import Employee


def pytest_assertrepr_compare(op, left, right):
    if op == "==":
        if isinstance(left, Employee) and isinstance(right, Employee):
            return [
                f"Comparing Employee instances:",
                f"   First Employee: {left.firstname} {left.lastname}, ID: {left.id}, Pay: {left.pay}",
                f"   Second Employee: {right.firstname} {right.lastname}, ID: {right.id}, Pay: {right.pay}",
                f"   Pay amounts are not equal: {left.pay} != {right.pay}",
            ]
