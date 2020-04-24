

def main():

    tempinit = 50
    veloinit = 0
    def windy(temp,velo):
        while velo != 55:
            windchill = 35.74 + (0.6215 * temp) - (35.75 * (velo ** .16)) + ((0.4275 * temp) * (velo ** 0.16))
            windchill = str(windchill)
            print(windchill[0:4], end=" ")
            print(velo)
            velo = velo + 5

    print(tempinit, windy(tempinit, veloinit))
            

    print("This program computes windchill")
    print()
    
    print("Temperature    " + "     " + "    Windchills")

    #print(str(tempinit) + "              " +  windy(tempinit,veloinit))
    


















main()
