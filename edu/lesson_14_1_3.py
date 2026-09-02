# Создаем пустой класс без атрибутов и методов
class Employee:
    pass


# Создаем сотрудников — уникальные объекты в памяти Python,
# которые созданы по шаблону Employee
emp_1 = Employee()
emp_2 = Employee()

# Выведем в консоль информацию и убедимся,
# что объекты уникальны в памяти компьютера
print(emp_1)
print(emp_2)

# Добавляем имя 1-му сотруднику
emp_1.first = "Ivan"
# Добавляем фамилию 1-му сотруднику
emp_1.last = "Ivanov"
# Добавляем email 1-му сотруднику
emp_1.email = "Ivan.Ivanov@email.com"
# Добавляем зарплату 1-му сотруднику
emp_1.pay = 50000

# Сделаем то же самое для второго сотрудника
# Добавляем имя 2-му сотруднику
emp_2.first = "Petr"
# Добавляем фамилию 2-му сотруднику
emp_2.last = "Petrov"
# Добавляем email 2-му сотруднику
emp_2.email = "Petr.Petrov@email.com"
# Добавляем зарплату 2-му сотруднику
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)


# Создаем класс c атрибутами
class Employee:
    first: str  # Здесь мы пишем название атрибута и указываем тип
    last: str
    pay: int
    email: str
