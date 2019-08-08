import turtle

class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color('white')
        self.pensize(5)
    def draw_border(self):
        self.penup()
        self.goto(-300,-300)
        self.pendown()
        self.goto(-300,300)
        self.goto(300,300)
        self.goto(300,-300)
        self.goto(-300,-300)
        self.hideturtle()