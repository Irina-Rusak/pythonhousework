"""
Практическое задание к уроку 8:
"""
"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год 
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, 
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:

    def __init__(self, date):
        self.date = date

    def day_month_year(self):
        try:
            day, month, year = self.date.split('-')
            return int(day), int(month), int(year)
        except Exception:
            print('Неверный формат даты!')

    @staticmethod
    def date_valid(date):
        try:
            day, month, year = date[0], date[1], date[2]
            if day < 1 or day > 31:
                raise Exception('день')
            if month < 1 or month > 12:
                raise Exception('месяц')
            if year < 1 or year > 2050:
                raise Exception('год')
            if day > 29 and month == 2:
                raise Exception('в феврале не более 29 дней')
        except Exception as e:
            print(f'Неверный формат даты ({e})!')
        else:
            print('Дата корректна.')


my_date = Date('06-11-2021')
my_date.date_valid(my_date.day_month_year())

my_date = Date('30-02-2021')
my_date.date_valid(my_date.day_month_year())

"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, 
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать 
эту ситуацию и не завершиться с ошибкой.
"""


class MyError(Exception):
    def __init__(self):
        self.txt = 'Деление на ноль запрещено!'


def division(x, y):
    try:
        if y == 0:
            raise MyError
        print(f'{x} / {y} = {x / y}')
    except MyError as e:
        print(e.txt)


division(100, 2)
division(100, 0)

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит 
работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем 
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
При этом работа скрипта не должна завершаться.
"""


class MyError(Exception):

    def __init__(self):
        self.text = 'Введено не число!'

    @staticmethod
    def check_int(user_string):
        if user_string.isdigit():
            return True
        else:
            return False


array_text = []
user_text = input('Введите строку только из чисел (для окончания ввода введите пустую строку): ')
while user_text:
    try:
        if MyError.check_int(user_text):
            array_text.append(user_text)
        else:
            raise MyError
    except MyError as err:
        print(err.text)
    user_text = input('Введите строку только из чисел (для окончания ввода введите пустую строку): ')

print(f'Полученный список: {array_text}')

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, 
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в 
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других 
данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, 
изученных на уроках по ООП.
"""


class Store:
    store_equipment = {'printer': {'HP 501': 10},
                       'PK': {'Lenovo 2000': 6}}

    @classmethod
    def store_add(cls, eq_type, model, count):
        eqip_type = cls.store_equipment.get(eq_type)
        if eqip_type:
            eq_type_model = cls.store_equipment[eq_type].get(model)
            if eq_type_model:
                print(f'Добавление техники {eq_type}, {model} в количестве {count} на склад.')
                cls.store_equipment[eq_type][model] += count
            else:
                print(f'Добавление техники {eq_type}, {model} в количестве {count} на склад.')
                cls.store_equipment[eq_type][model] = count
        else:
            print(f'Добавление техники {eq_type}, {model} в количестве {count} на склад.')
            cls.store_equipment[eq_type][model] = count

    @classmethod
    def store_sub(cls, eq_type, model, count):
        eqip_type = cls.store_equipment.get(eq_type)
        if eqip_type:
            eq_type_model = cls.store_equipment[eq_type].get(model)
            if eq_type_model:
                if cls.store_equipment[eq_type][model] < count:
                    print(f'Недостаточно техники тип: {eq_type}, модель: {model} на складе. '
                          f'Есть всего {cls.store_equipment[eq_type][model]} шт.')
                else:
                    print(f'Удаление техники {eq_type}, {model} в количестве {count} со склада.')
                    cls.store_equipment[eq_type][model] -= count
            else:
                print(f'Техники тип: {eq_type}, модель: {model} нет на складе.')
        else:
            print(f'Техники тип: {eq_type}, модель: {model} нет на складе.')


class OfficeEquipment:
    def __init__(self, type, model, count):
        try:
            self.type = type
            self.model = model
            self.count = int(count)
        except Exception:
            print('Введено неверное количество позиций техники.')


class Printer(OfficeEquipment):
    def __init__(self, type, model, count, color):
        super().__init__(type, model, count)
        self.color = color
        Store.store_add('printer', model, count)


class PK(OfficeEquipment):
    def __init__(self, type, model, count, system):
        super().__init__(type, model, count)
        self.system = system
        Store.store_add('PK', model, count)


print(Store.store_equipment)
printer_1 = Printer('printer', 'HP 501', 10, 'white')
printer_2 = Printer('printer', 'Samsung 120', 20, 'black')
print(Store.store_equipment)

pk_1 = PK('PK', 'Asus', 50, 'Windows')
print(Store.store_equipment)

Store.store_sub('PK', 'Asus', 10)
print(Store.store_equipment)

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку 
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) 
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        return f"{self.a} + {self.b}i"


number_1 = Complex(15, 2)
number_2 = Complex(-2, 4)
print(f'Сумма комплексных чисел {number_1.a} + {number_1.b}i и {number_2.a} + {number_2.b}i = {number_1 + number_2}')
print(f'Произведение комплексных чисел {number_1.a} + {number_1.b}i и {number_2.a} + {number_2.b}i = '
      f'{number_1 * number_2}')
