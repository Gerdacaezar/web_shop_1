class Employee:
    """Класс для представления сотрудника"""

    def __init__(self, first, last, pay):
        self.first = first  # Эквивалентно emp_1.first = 'Ivan'
        self.last = last  # Эквивалентно emp_1.last = 'Ivanov'
        self.pay = pay  # Эквивалентно emp_1.pay = 50000
        self.email = f"{first}.{last}@email.com"  # Эквивалентно emp_1.email = 'Ivan.Ivanov@email.com
