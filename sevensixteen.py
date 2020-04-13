from graphics import *

def main():
    win = GraphWin()
    aCircle = Circle(Point(100,100), 10)
    bCircle = Circle(Point(100,100), 20)
    cCircle = Circle(Point(100,100), 30)
    dCircle = Circle(Point(100,100), 40)
    eCircle = Circle(Point(100,100), 50)
    eCircle.setOutline("black")
    dCircle.setFill("black")
    cCircle.setFill("blue")
    bCircle.setFill("red")
    aCircle.setFill("yellow")
    eCircle.draw(win)
    dCircle.draw(win)
    cCircle.draw(win)
    bCircle.draw(win)
    aCircle.draw(win)

    points = 0


    P1 = win.getMouse()

    if P1.getX() <= 110 and P1.getX() >= -110 and P1.getY() <= 110 and P1.getY() >= -110:
        points = 9
        print(points)
    elif P1.getX() <= 120 and P1.getX() >= -120 and P1.getY() <= 120 and P1.getY() >= -120:
        points = 7
        print(points)
    elif P1.getX() <= 130 and P1.getX() >= -130 and P1.getY() <= 130 and P1.getY() >= -130:
        points = 5
        print(points)
    elif P1.getX() <= 140 and P1.getX() >= -140 and P1.getY() <= 140 and P1.getY() >= -140:
        points = 3
        print(points)
    elif P1.getX() <= 150 and P1.getX() >= -150 and P1.getY() <= 150 and P1.getY() >= -150:
        points = 1
        print(points)
    else:
        points = 0
        print("No Points!")
    
    
main()
