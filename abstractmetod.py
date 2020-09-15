class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        raise NotImplementedError('Собака має гавкати')


class Puppy(Dog):

    def bark(self):
        print("тяв")


class Bigdog(Dog):

    def bark(self):
        print("ГАУУУ")


class Buldog(Dog):

    def play(self):
        print('playing')


a = Puppy('Mimi', 0.5)
a.bark()
b = Bigdog('Jek', 10)
b.bark()
c = Buldog('Kim', 15)
