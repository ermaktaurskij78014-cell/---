class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return self.name + " издаёт звук"

    def info(self):
        return "Имя: " + self.name + ", Возраст: " + str(self.age)


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return self.name + " лает: Гав!"

    def fetch(self):
        return self.name + " принёс мяч"

    def info(self):
        b = super().info()
        return b + ", Порода: " + self.breed


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):
        return self.name + " мяукает"

    def purr(self):
        return self.name + " мурлычет"

    def info(self):
        b = super().info()
        t = "домашняя" if self.indoor else "уличная"
        return b + ", " + t


a = Animal("Животное", 5)
d = Dog("Бобик", 3, "Овчарка")
c = Cat("Мурка", 2, True)

animals = [a, d, c]

for x in animals:
    print(x.speak())

print()
for x in animals:
    print(x.info())

print()
print(d.fetch())
print(c.purr())

print()
print("Dog is Animal:", isinstance(d, Animal))
print("Cat is Dog:", isinstance(c, Dog))
