import turtle

class Score(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.goto(-290,310)
        self.score=0
        self.write("Score: {}".format(self.score), False, align="left", font=("Arial", 14, "normal"))

    def endgame(self):
        self.clear()
        self.goto(0,0)
        self.write("YOU WIN!", False, align="center", font=("Arial", 14, "normal"))
        self.goto(0,-20)
        self.write("YOUR SCORE: {}".format(self.score), False, align="center", font=("Arial", 14, "normal"))

    def updateScore(self):
        self.clear()
        self.write("SCORE: {}".format(self.score), False, align="left", font=("Arial", 14, "normal"))
        
    def changeScore(self):
        self.score+=10
        self.updateScore()