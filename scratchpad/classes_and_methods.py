class Car:
     def __init__(self, make, model_name, top_speed, color):
       self.make = make
       self.model_name = model_name
       self.top_speed = top_speed
       self.color = color
     def __str__(self):
        return f'{self.color} {self.make} {self.model_name}'
     def __repr__(self):
        return f"Car(make={self.make} model={self.model_name}, top_speed={self.top_speed}, color={self.color})"
     def __eq__(self, other):
        return (
        self.make == other.make and
        self.model_name == other.model_name and
        self.top_speed == other.top_speed and
        self.color == other.color
        )
     def __eq__(self, other):
        return all(
        (
        self.make == other.make,
        self.model_name == other.model_name,
        self.top_speed == other.top_speed,
        self.color == other.color
        )
        )
car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_two = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
car_one == car_two
print (car_one == car_two)

car_three = Car(make="Ford", model_name="Mustang", top_speed=250, color="Yellow")
car_one == car_three
print (car_one == car_three)
#car_one = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
#car_two = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")
#car_one == car_two
#print (car_one == car_two)

#mustang = Car(make="Ford", model_name="Mustang", color="Yellow", top_speed=250)
#car = Car(make="Ford", model_name="Mustang", top_speed=250, color="Red")

#print (mustang)
#print (car)