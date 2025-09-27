import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    cars=[]
    def create_car(self):
        random_no = random.randint(0, 6)
        if random_no == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(280,random.randint(-250,250))
            car.left(180)
            self.cars.append(car)
    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)


