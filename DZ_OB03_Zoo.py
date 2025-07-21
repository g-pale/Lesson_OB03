import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Какой-то общий звук животного.")

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит.")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит.")

# Полиморфизм
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Сотрудники
class Employee:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Зоопарк с композицией
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        data = {
            'animals': [
                {'type': animal.__class__.__name__, 'name': animal.name, 'age': animal.age}
                for animal in self.animals
            ],
            'employees': [
                {'type': employee.__class__.__name__, 'name': employee.name}
                for employee in self.employees
            ]
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.animals.clear()
            self.employees.clear()
            for a in data['animals']:
                if a['type'] == 'Bird':
                    animal = Bird(a['name'], a['age'], wing_span=0)
                elif a['type'] == 'Mammal':
                    animal = Mammal(a['name'], a['age'], fur_color='неизвестно')
                elif a['type'] == 'Reptile':
                    animal = Reptile(a['name'], a['age'], scale_type='неизвестно')
                else:
                    animal = Animal(a['name'], a['age'])
                self.animals.append(animal)
            for e in data['employees']:
                if e['type'] == 'ZooKeeper':
                    employee = ZooKeeper(e['name'])
                elif e['type'] == 'Veterinarian':
                    employee = Veterinarian(e['name'])
                else:
                    employee = Employee(e['name'])
                self.employees.append(employee)

# Демонстрация
if __name__ == "__main__":
    zoo = Zoo()
    bird = Bird("Попугай", 2, 0.25)
    mammal = Mammal("Тигр", 5, "оранжевый")
    reptile = Reptile("Змея", 3, "гладкая")

    zookeeper = ZooKeeper("Анна")
    vet = Veterinarian("Доктор Федоров")

    zoo.add_animal(bird)
    zoo.add_animal(mammal)
    zoo.add_animal(reptile)

    zoo.add_employee(zookeeper)
    zoo.add_employee(vet)

    print("\nЗвуки животных в зоопарке:")
    animal_sound(zoo.animals)

    print("\nРабота сотрудников:")
    zookeeper.feed_animal(mammal)
    vet.heal_animal(reptile)

    zoo.save_to_file("записи_зоопарка.json")

    # Для проверки загрузки
    # new_zoo = Zoo()
    # new_zoo.load_from_file("записи_зоопарка.json")
