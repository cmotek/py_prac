import math
from graphics import *


def main():

    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)


    def square(x):
        return x ** 2

    def distance1(p1,p2):
        dist1 = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
        return dist1

    def distance2(p2,p3):
        dist2 = math.sqrt(square(p3.getX() - p2.getX()) + square(p3.getY() - p2.getY()))
        return dist2

    def distance3(p1,p3):
        dist3 = math.sqrt(square(p1.getX() - p3.getX()) + square(p1.getY() - p3.getY()))
        return dist3


    def trianglemaker(dist1,dist2,dist3):
        

        
        s = (dist1 + dist2 + dist3)/2

        A = math.sqrt(s * (s - dist1) * (s - dist2) * (s - dist3))

        return A


    print(trianglemaker(distance1(p1,p2),distance2(p2,p3),distance3(p1,p3)))

    












main()
