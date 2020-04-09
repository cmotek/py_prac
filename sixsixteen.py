from graphics import *




def main():

    win = GraphWin("FRIENDS", 500,500)
    friendsImage = Image(Point(250,250), "friends.png")
    friendsImage.draw(win)

    headsize = 50

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


    for i in range(6):
        nose = win.getMouse()
        drawFace(nose,headsize,win)



main()
