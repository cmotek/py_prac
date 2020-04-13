


def main():


    weight = int(input("Please provide your weight in lbs:"))
    height = int(input("Please provide your height in inches:"))
    BMI = (weight * 720)/(height ** 2)
    if BMI < 19:
        print("Your BMI is too low and unhealthy!")
    if BMI >= 19 and BMI <= 25:
        print("Your BMI is in a healthy range!")
    if BMI > 25:
        print("Your BMI is too high and unhealthy!")







main()
