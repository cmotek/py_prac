from graphics import *

def main():
    win = GraphWin()
    Text(Point(20,20), "    Principal:").draw(win)
    Text(Point(20,50), "    APR:").draw(win)
    princput = Entry(Point(80,20), 5)
    aprput = Entry(Point(80,50), 5)
    princput.setText("0.0")
    aprput.setText("0.0")
    princput.draw(win)
    aprput.draw(win)



    win.getMouse()
    princout = int(princput.getText())
    aprput = float(aprput.getText())

    for year in range(1,11):
        principal = princout * (1 + aprput)
        

    print("The value in 10 years is:", principal)



main()
