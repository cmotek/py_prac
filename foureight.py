from graphics import *
import math

def main():
    win = GraphWin("foureight")
    point1 = win.getMouse()
    point2 = win.getMouse()
    win.plot(((point2.getX() + point1.getX())/2), ((point2.getY() + point1.getY())/2), "cyan")
    drawnline = Line(point1, point2)
    drawnline.draw(win)
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    slope = dy/dx
    print("Slope is: ", slope)
    length = math.sqrt((dx * dx) + (dy * dy))
    print("The length of the line: ", length)
    




main()
