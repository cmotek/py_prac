

def main():

    tempinit = -20
    veloinit = 50
    def windy(temp,velo):


        
        while velo != -5:
            chills = []
            while temp != 70:
                windchill = str(35.74 + (0.6215 * temp) - (35.75 * (velo ** .16)) + ((0.4275 * temp) * (velo ** 0.16)))[0:6]
                chills.append(windchill)
                temp = temp + 10
            print(velo,chills)
            temp = -20
            velo = velo - 5

    
              
        
        
            

            

    print("This program computes windchill")
    print()
    
    print("Wind Speed    " + "     " + "    Windchills")

    windy(tempinit, veloinit)

    print("Temp: -20       -10        0        10        20        30        40        50        60")





main()
