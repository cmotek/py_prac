def main():

    infileName = input("What is the dang filename?:")
    infile = open(infileName, "r")
    print(infileName)


    
    numofwords = 0
  
    filereader = infile.read()
    wordcounter = filereader.split()
    numofwords = len(wordcounter)
    characters = len(filereader)

    lines = infile.readlines()
    counter = len(lines) + 1


    
    print("The number of words is: ",numofwords)
    print("The number of characters is: ", characters)
    print("The number of lines is: ", counter)

    














main()
