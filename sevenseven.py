


def main():

    startingtime = float(input("What was the starting time?:").replace(":","."))
    endingtime = float(input("What was the ending time?:").replace(":","."))
    pastninemoney = 0
    regularhoursmoney = 0
    totalsittingpayment = 0 
    if endingtime > 9.0:
        pastninemoney = (endingtime - 9.0) * 1.75
        regularhoursmoney = (9.0 -  startingtime) * 2.50
        totalsittingpayment = pastninemoney + regularhoursmoney
        print(totalsittingpayment)
    if endingtime <= 9.0:
        regularhoursmoney = (endingtime - startingtime) * 2.50
        print(regularhoursmoney)
 



main()
