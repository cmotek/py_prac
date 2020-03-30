



def main():

    s1 = "spam"
    s2 = "ni!"

    print("The Knights who say, " + s2)
    print(3 * s1 + 2 * s2)
    print(s1[1])
    print(s1[1:3])
    print(s1[2] + s2[:2])
    print(s1 + s2[-1])
    print(s1.upper())
    print(s2.upper().ljust(4) * 3)

    print(s2[0:2].upper())
    print(s2 + s1 + s2)
    print((" " + s1.capitalize() + " " + s2.capitalize()) * 3)
    print(s1)
    print([s1[:2], s1[3]])
    print(s1.replace("a", ""))
    
    
    for ch in "aardvark":
        print(ch)

    for w in "Now is the winter of our discontent...".split():
        print(w)

    for w in "Mississippi".split("i"):
        print(w, end=" ")

    print()
    
    msg = ""
    for s in "secret".split("e"):
        msg = msg + s
    print(msg)

    msg = ""
    for ch in "secret":
        msg = msg + chr(ord(ch) + 1)
    print(msg)

    print("Looks like {1} and {0} for breakfast".format("eggs","spam"))
    print("There is {0}{1}{2}{3}".format(1,"spam", 4, "you"))
    print("Hello {0}".format("Susan", "Computewell"))
    print("{0:0.2f} {0:0.2f}".format(2.3, 2.3468))
    #print("{7.5f} {7.5f}".format(2.3, 2.3468))
    print("Time left {0:02}:{1:05.2f}".format(1, 37.374))
    #print("{1:3}".format("14"))





main()
