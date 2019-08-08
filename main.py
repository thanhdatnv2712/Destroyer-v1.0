import turtle
import time
import math
import random
import os
import time
from threading import Thread
import threading
from heros import Heros
from border import Border
from monster import Monsters
from score import Score

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False

if __name__ == "__main__":
    path = os.getcwd()
    screen = turtle.Screen()
    screen.setup(700,700)
    screen.bgpic(path + "/image/background.png")
    screen.title('Destroyer v1.0')
    # make Heros
    player = Heros(screen)
    turtle.listen()
    turtle.onkey(player.turnleft, 'Left')
    turtle.onkey(player.turnright,'Right')
    turtle.onkey(player.accelerate,'Up')
    turtle.onkey(player.deccelerate,'Down')
    # make Border
    border = Border()
    border.draw_border()
    # Compute Score
    score = Score()
    #Init Monsters
    monsterbox = []
    for i in range(random.randint(6, 12)):
        monsterbox.append(Monsters(screen))
    #Process
    check = False
    while True:
        # t = threading.Thread(target = player.move, args= ())
        player.move()
        # t.start()
        # t.join()
        for qv in monsterbox:
            qv.move()
            # t1 = threading.Thread(target = qv.move, args= ())
            # t1.start()
            # t1.join()
            if isCollision(player, qv):
                monsterbox.remove(qv)
                qv.hideturtle()
                score.changeScore()
                if len(monsterbox) == 0:
                    check = True
        if check:
            player.hideturtle()
            score.endgame()
            time.sleep(5)
            break


