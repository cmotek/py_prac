from graphics import *

def main():

    infileName = input("What is the dang filename?:")
    infile = open(infileName, "r")

    numofstudents = infile.readline()
    print(numofstudents)
    gradelist = infile.readlines()
    print(gradelist)















main()
