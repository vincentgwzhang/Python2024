class Animal(object):
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        print('Cat speak function triggered')

class Dog(Animal):
    def speak(self):
        print('Dog speak function triggered')

class Other(object):
    def speak(self):
        print("Other speak function triggered")

def speak(object):
    object.speak()

# Cat().speak()
# Dog().speak()
speak(Dog())
speak(Other())