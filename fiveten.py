



def main():

    lengthofwords = []
    counter = 0 
    sentence = input("Please input a sentence:")
    numberofwords  = sentence.split()
    for ch in numberofwords:
        lengthofwords.append(len(ch))
    print(lengthofwords)
    for ch in lengthofwords:
        counter = counter + ch
    averagetotal = counter/len(numberofwords)
    print(averagetotal)




main()
