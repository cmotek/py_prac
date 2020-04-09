from graphics import *




def main():
    
    window = GraphWin()
    headsize = 40
    nose = window.getMouse()
    
    def drawFace(center,size,win):
        
        hair = Circle(Point(center.getX(),center.getY() - 30), 55)
        hair.setFill("brown")
        hair.draw(win)

        face = Circle(center, size)
        face.setFill("peachpuff")
        face.setOutline("black")
        face.draw(win)
        leye = Circle(Point(center.getX() - 13, center.getY() - 5), 2.5)
        reye = Circle(Point(center.getX() + 13, center.getY() - 5), 2.5)
        leye.setFill("blue")
        reye.setFill("blue")
        leye.draw(win)
        reye.draw(win)

        
        mouth = Circle(Point(center.getX(), center.getY() + 20), 12)
        mouth.setOutline("black")
        mouth.setFill("black")
        mouth.draw(win)

    drawFace(nose,headsize,window)
    
        


main()
