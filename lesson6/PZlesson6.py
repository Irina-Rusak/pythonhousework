"""
Практическое задание к уроку 6:
"""
"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: 
красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, 
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в 
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение 
и завершать скрипт.
"""
import time


class TrafficLight:

    def __init__(self, __color, second):
        self.__color = __color
        self.second = second

    def running(self):
        print(f'{self.__color}')
        time.sleep(self.second)


light_red = TrafficLight('red', 7)
light_yellow = TrafficLight('yellow', 2)
light_green = TrafficLight('green', 5)

try:
    while True:
        light_red.running()
        if light_red._TrafficLight__color == 'red':
            light_yellow.running()
            if light_yellow._TrafficLight__color == 'yellow':
                light_green.running()
                if light_green._TrafficLight__color != 'green':
                    raise Exception('Ошибка в режиме.')
            else:
                raise Exception('Ошибка в режиме.')
        else:
            raise Exception('Ошибка в режиме.')
except Exception as e:
    print(e)

"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calc_mass_asphalt(self, mass_asphalt_unit=25, thickness=5):
        if mass_asphalt_unit != 25 or thickness != 5:
            print(f'Скорректированы расчетные показатели для следующего расчета:\n'
                  f'- масса асфальта для покрытия 1 кв.м. дороги = {mass_asphalt_unit} кг.\n'
                  f'- толщины полотна = {thickness} см.')
        return int(self._length * self._width * mass_asphalt_unit * thickness)


road_a = Road(5000, 20)
print(f'Масса асфальта для дороги (длина = {road_a._length} м., ширина = {road_a._width} м.): '
      f'{road_a.calc_mass_asphalt()} кг.')
print(f'Масса асфальта для дороги (длина = {road_a._length} м., ширина = {road_a._width} м.): '
      f'{road_a.calc_mass_asphalt(mass_asphalt_unit=24.5, thickness=7)} кг.')

road_b = Road(2000, 40)
print(f'Масса асфальта для дороги (длина = {road_b._length} м., ширина = {road_b._width} м.): '
      f'{road_b.calc_mass_asphalt()} кг.')

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), 
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, 
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии 
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, 
проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:

    def __init__(self, name, surname, position, **kwargs):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage, self.bonus = int(kwargs['wage']), int(kwargs['bonus'])
        self.total_income = self.wage + self.bonus


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.total_income


worker_1 = Position('Ivan', 'Ivanov', 'Manager', wage=50000, bonus=15000)
print(f'Name of worker: {worker_1.get_full_name()}')
print(f'Total income = {worker_1.get_total_income()}')

worker_2 = Position('Petr', 'Petrov', 'Director', wage=100000, bonus=30000)
print(f'Name of worker: {worker_2.get_full_name()}')
print(f'Total income = {worker_2.get_total_income()}')

"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, 
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, 
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала.')

    def stop(self):
        print('Машина остановилась.')

    def turn(self, direction):
        print(f'Машина повернула {direction}.')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км.')


class TownCar(Car):

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км.') if int(self.speed) <= 60 else \
            print(f'Превышение скорости на {int(self.speed) - 60} км. (норма - 60).')


class SportCar(Car):

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км.')


class WorkCar(Car):

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed}.') if int(self.speed) <= 40 else \
            print(f'Превышение скорости на {int(self.speed) - 40} км. (норма - 40).')


class PoliceCar(Car):

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.speed} км.')


car_1 = TownCar(40, 'красный', 'KIA', False)
print(f'Авто: {car_1.name}, цвет авто: {car_1.color}, скорость: {car_1.speed}.')
car_1.go()
car_1.turn('направо')
car_1.stop()
car_1.show_speed()

car_2 = WorkCar(45, 'синий', 'Mazda', False)
print(f'Авто: {car_2.name}, цвет авто: {car_2.color}, скорость: {car_2.speed}.')
car_2.go()
car_2.turn('налево')
car_2.stop()
car_2.show_speed()

car_3 = SportCar(90, 'черный', 'BMW', False)
print(f'Авто: {car_3.name}, цвет авто: {car_3.color}, скорость: {car_3.speed}.')
car_3.go()
car_3.turn('направо')
car_3.stop()
car_3.show_speed()

car_4 = PoliceCar(70, 'бело-красный', 'Opel', True)
print(f'Авто: {car_4.name}, цвет авто: {car_4.color}, скорость: {car_4.speed}.')
car_4.go()
car_4.turn('налево')
car_4.stop()
car_4.show_speed()

"""
5. Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное 
сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск тонкой отрисовки ({self.title}).')


class Pencil(Stationery):

    def draw(self):
        print(f'Запуск полужирной отрисовки ({self.title}).')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск жирной отрисовки ({self.title}).')


pen = Pen('ручка')
pen.draw()

pencil = Pencil('карандаш')
pencil.draw()

handle = Handle('маркер')
handle.draw()
