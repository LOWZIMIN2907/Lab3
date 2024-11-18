import employee_info as info

def test_get_employee_by_age_range():
    result = []
    result = info.get_employees_by_age_range(20, 30)
    expected_result = [{'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000}, {'name': 'Mary', 'age': 23, 'department': 'Marketing', 'salary': 56000}]
    assert result == expected_result

def test_average_salary():
    result = 0
    expected_average = (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6
    result = info.calculate_average_salary()
    assert result == expected_average

def test_get_employee_by_dept():
    result = []
    result = info.get_employees_by_dept("Sales")
    expected_result = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]
    assert result == expected_result