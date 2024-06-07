# https://stackabuse.com/object-oriented-programming-in-python/

# Creates class Car
class Car:

    # create class attributes
    name = "c200"
    make = "mercedez"
    model = 2008

    # create class methods
    def start(self):
        print ("Engine started")

    def stop(self):
        print ("Engine switched off")

car_obj = Car()

print(car_obj.name)

car_obj.start()
car_obj.stop()


