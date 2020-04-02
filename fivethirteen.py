






def main():

    infileName = input("What is the dang filename?:")
    infile = open(infileName, "r")
    print(infileName)


    
    numofwords = 0
  
    filereader = infile.read()
    wordcounter = filereader.split()
    numofwords = len(wordcounter)
    print(numofwords)














main()
