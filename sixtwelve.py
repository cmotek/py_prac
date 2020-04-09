

def main():

    numlist = [3,4,5,6,7,8,9]

    def sumList(nums):
        countnums = 0
        for i in nums:
            countnums = countnums + i
        return countnums


    print(sumList(numlist))



main()
