import time
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT = 180
tre = 300
speed = 0


class CarManager(Turtle):

    def __init__(self):
        super().__init__()

        self.segments = []
        self.create_car()
        self.penup()
        self.head = self.segments[0]
        self.car_speed = MOVE_INCREMENT


    def drive(self):
        # x = self.xcor() - STARTING_MOVE_DISTANCE
        # y = self.y_position
        # self.goto(x, y)
        # car = CarManager()
        for seg_num in range(len(self.segments)-1, 0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(self.car_speed)


    def create_car(self):
        self.car_segments()
        y_position = random.randint(-280, 280)
        temp = y_position
        x_position = 300
        for i in range(len(self.segments)):
            self.segments[i].goto(x_position, temp)
            x_position += MOVE_INCREMENT

    def car_segments(self):
        temp_color = random.choice(COLORS)

        for _ in range(1):
            car = Turtle("square")
            car.penup()
            car.color(temp_color)
            car.setheading(LEFT)
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.segments.append(car)

    def add_speed(self):
        self.car_speed += MOVE_INCREMENT











        # self.shapesize(stretch_wid=1, stretch_len=1)






