


def main():

    startnumber = eval(input("Please input the starting number:"))

    def syracuse(syr_number):

        syr_list = [syr_number]

        while syr_number != 1:

            if syr_number % 2 == 0:
                syr_number = syr_number/2
            else:
                syr_number = (3 * syr_number) + 1

            syr_list.append(int(syr_number))


        print(syr_list)



    syracuse(startnumber)







main()
