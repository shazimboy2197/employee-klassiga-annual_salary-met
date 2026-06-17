class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12
```

```python
# Misol:
employee = Employee("John Doe", 5000)
print(employee.annual_salary())  # Chiqaradi: 60000
