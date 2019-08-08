import turtle
import random
import os

class Monsters(turtle.Turtle):
    def __init__(self, sc):
        turtle.Turtle.__init__(self)
        
        self.penup()
        self.speed(0)
        sc.addshape(os.getcwd() + "/image/2v2.gif")
        self.shape(os.getcwd() + "/image/2v2.gif")
        # self.shape("circle")
        # self.color("red")
        self.speed=3
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))
    def jump(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))
    def die(self):
        self.penup()
    def move(self):
        self.forward(self.speed)
        if self.xcor()>290:
            self.setx(290)
            self.right(60)
        if self.xcor()<-290:
            self.setx(-290)
            self.right(60)
        if self.ycor()>290:
            self.sety(290)
            self.right(60)
        if self.ycor()<-290:
            self.sety(-290)
            self.right(60)