


def main():

    def numreader(filename):
        infile = open(filename, "r")
        filetext = infile.read()
        filetext = filetext.split()
        newints = []
        countnums = 0
        for i in filetext:
            newints.append(int(i)**2)
        for t in newints:
            countnums = countnums + t
        return countnums
            

    filename = input("What is the filename?:")


    print(numreader(filename))




main()
