from graphics import *

win = GraphWin('Shapes')
center = Point(100,100)
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)

label = Text(center, "Red Circle")
label.draw(win)

rect = Rectangle(Point(30,30), Point(70,70))
rect.draw(win)

line = Line(Point(20,30), Point(180, 165))
line.draw(win)

oval = Oval(Point(20,150), Point(180,199))
oval.draw(win)

win = GraphWin("Tic-Tac-Toe")
win.setCoords(0.0, 0.0, 3.0, 3.0)
Line(Point(1,0), Point(1,3)).draw(win)
Line(Point(2,0), Point(2,3)).draw(win)

Line(Point(0,1), Point(3,1)).draw(win)
Line(Point(0,2), Point(3,2)).draw(win)
