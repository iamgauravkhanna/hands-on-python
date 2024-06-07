class Dog:

    which_type = 'mammal'

    def __init__(self, name) :
        self.name = name

    def speak(self) :
        print("I am {}".format(self.name))

dog = Dog("Tommy")

dog.speak()

print( "My Type is", dog.which_type)