



def main():

     def Sum(n):
         sum = int(0) 
         for i in range(int(n)+1):
             sum = sum + i
         print(sum)
             

     def sumNCubes(n):
         sum = int(0)
         for i in range(int(n)+1):
             sum = sum + (i * i * i)
         print(sum)

     n = input("Please provide the n:")

     
     Sum(n)
     sumNCubes(n)



main()
