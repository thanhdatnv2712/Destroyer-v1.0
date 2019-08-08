import turtle
import os

class Heros(turtle.Turtle):
    def __init__(self, sc):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        # sc.register_shape(os.getcwd() + "/image/hero.png")
        sc.addshape(os.getcwd() + "/image/1v2.gif")
        self.shape(os.getcwd() + "/image/1v2.gif")
        # self.color('white')
        self.speed = 1

    def move(self):
        self.forward(self.speed)
        if self.xcor() > 290:
            self.setx(290)
            self.right(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.right(60)
        if self.ycor() > 290:
            self.sety(290)
            self.right(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.right(60)
        
    def turnleft(self):
        self.left(30)
    def turnright(self):
        self.right(30)
    def accelerate(self):
        self.speed += 1
    def deccelerate(self):
        self.speed -= 1
