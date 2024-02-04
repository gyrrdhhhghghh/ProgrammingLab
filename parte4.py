import random

class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def __str__(self):
        return 'person: {}, {}'.format(self.name, self.surname)

    def say_hi(self):
        random_number = random.randint(0,2)
        if random_number == 0:
            print('hi!')
        if random_number == 1:
            print('hello')
        if random_number == 2:
            print('good morning')

mario = Person('mario', 'rossi')
mario.say_hi()

class Student(Person):
    def __str__(self):
        return 'student: {}, {}.'.format(self.name, self.surname)

class Professor(Person):
    def __str__(self):
        return 'prof. {}, {}.'.format(self.name, self.surname)
    def say_hi(self):
        print('hello, i am professor {}'.format(self.surname))

    def original_say_hi(self):
        super().say_hi()