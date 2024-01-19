class Dog:

    which_type = 'mammal'

    def __init__(self, name) :
        self.name = name

    def speak(self) :
        print("I am {}".format(self.name))

tommy = Dog("Tommy")

tommy.speak()
print( "My Type is ", tommy.which_type)