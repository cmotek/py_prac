import math

#print("Volume & Surface Area")
#r = int(input("Give me a dang radius: "))
#V = (4 / 3) * (math.pi) * (r ** 3)
#V = str(V)
#print("Volume is:" + V)
#A = 4 * (math.pi) * (r ** 2)
#A = str(A)
#print("Surface Area is:" + A)

#print("THIS IS A DANG PIZZA PRICER BY SQUARE INCH")
#d = int(input("Give me a dang pizza diameter in inches: "))
#c = float(input("Give me a dang price of the whole pizza: "))
#sqrinch = round((c / ((math.pi) * ((d / 2) ** 2))), 2)
#print("The pizza costs " + str(sqrinch) + " per square inch.")

#print("THIS IS A DANG MOLECULAR WEIGHT TOTALIZER")
#C = int(input("Please provide the number of carbon atoms: "))
#H = int(input("Please provide the number of hydrogen atoms: "))
#O = int(input("Please provide the number of oxygen atoms: "))
#total = round((12.0107 * C) + (1.00794 * H) + (15.9994 * O), 2)
# print("This is the totalized molecular weight of all those atoms combined: " + str(total) + " grams per mole")

#print("THIS WILL CALCULATE THE DISTANCE BETWEEN YOURSELF AND A PIECE OF LIGHTNING")
#s = input("How many seconds has it been since you saw the lightning? ")
#d = round(((float(s) * 1100) / 5280), 2)
#print("The lightning piece was " + str(d) + " miles away from your body!")

#c = int(input("Please indicate how many pounds of coffee you intend to purchase: "))
#cship = (10.50 * c) + (0.86 * c) + 1.50
#print("Your dang total is  $" + str(cship))

#x1, y1 = (int(t) for t in (input("Please provide a point: ").split()))
#x2, y2 = (int(t) for t in (input("Please provide an additional point: ").split()))
#SLOPE = (y2 - y1)/(x2 - x1)
#print("Here's the slope of those points FYI: " + str(SLOPE))

#x1, y1 = (int(t) for t in (input("Please provide a point: ").split()))
#x2, y2 = (int(t) for t in (input("Please provide an additional point: ").split()))
#distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
#print("Here's the distance betweeen those points FYI: " + str(distance))

#year = int(input("Please enter the year: "))
#C = year//100
#epact = (8 + (C//4) - C + ((8 * C + 13)//25) + 11 * (year % 19)) % 30
#print("This is, supposedly, the epact of that year: " + str(epact))

#s1, s2, s3 = (int(t) for t in (input("Please provide 3 side lengths: ").split()))
#s = (s1 + s2 + s3) / 2
#A = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
#print("This is the area of that triangle: " + str(A))

#height = int(input("Now how tall is the house? " ))
#angle = int(input("And what angle was the ladder placed at when leaning against said house? "))
#radians = (math.pi / 180) * angle
#ladder = height / math.sin(radians)
#print("That ladder was " + str(ladder) + " feet long!")

#n = int(input("Okay please give me n: "))
#sumn = (n * (n + 1)) / 2
#print(str(sumn) + " is the sum of n natural numbers boom")

#n = int(input("Okay please give me n: "))
#sumn = ((n * (n + 1)) / 2) ** 2
#print(str(sumn) + " is the sum of n natural numbers cubed boom")

#n = int(input("Okay so how many numbers do you want to add up? "))
#total = 0
#for i in range(n):
#        x = int(input("Okay then give me a number!"))
#        total = total + x
#print("Well this is your dang total, it's: " + str(total))

#n = int(input("Okay so how many numbers do you want to average out? "))
#total = 0
#for i in range(n):
#        x = int(input("Okay then give me a number!"))
#        total = total + x
#average = total / n
#print("Well this is your dang average, it's: " + str(average))

#n = int(input("Okay so how many terms do you want to sum I guess to approximate pi?"))
#approxpi = 0
#for i in range(n):
#    if (i % 2 == 0):
#        approxpi = approxpi + (4/(i + (i + 1)))
#    else:
#        approxpi = approxpi + ((-1) * (4/(i + (i + 1))))
#
#diff = math.pi - approxpi

#print("Okay this is approximately pi: " + str(approxpi))
#print(diff)
#print(math.pi)

#d = int(input("Okay lets do a dang fibonannci sequence, how many numbers? "))
#a, b = 0, 1
#for i in range(d):
#    print(b)
#    a, b = b, a+b

v = int(input("What value do you want to find the exciting square root of? "))
d = int(input("How many guess shots you get? "))
guess = v / 2
for i in range(d):
       guess = (guess + (v / guess)) / 2
print(guess)

diff = math.sqrt(v) - guess
print(math.sqrt(v), guess, diff)


