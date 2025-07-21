# Создайте класс Animal с методом make_sound(). Затем создайте несколько
# дочерних классов (например, Dog, Cat, Cow), которые наследуют Animal,
# но изменяют его поведение (метод make_sound()). В конце создайте список
# содержащий экземпляры этих животных и вызовите make_sound() для каждого животного в цикле.

class Animal():
    def make_sound(self):
        print("Making sound")

class Dog(Animal):
    def make_sound(self):
        print('Собака лает')

class Cat(Animal):
    def make_sound(self):
        print("Мяукает")

class Cow(Animal):
    def make_sound(self):
        print("Мычит")

list_of_animals = [Dog(), Cat(), Cow()]
for animal in list_of_animals:
    animal.make_sound()


