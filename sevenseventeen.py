from graphics import *
import random

def main():

    
    win = GraphWin()

    dx = 1
    dy = 1

    aCircle= Circle(Point(49,68), 10)
    aCircle.draw(win)
    
    for i in range(1000000000):

        aCircle.move(dx,dy)
       

        circleCenter = aCircle.getCenter()
        
        if circleCenter.getY() == 200.0:
            dy = -1
        if circleCenter.getY() == 0.0:
            dy = 1
        if circleCenter.getX() == 200.0:
            dx = -2
        if circleCenter.getX() == 0.0:
            dx = 1


       
  


main()
