


def main():


    numlist = ['1','2','3','4','5']


    def toNumbers(strList):
        newints = []
        for i in strList:
            newints.append(int(i))
        return newints


    print(toNumbers(numlist))




main()
