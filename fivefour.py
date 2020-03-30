



def main():
    acronym = input("Give me your acronym phrase:")
    newacronym = []
    for i in acronym.split():
        thing = i[0]
        newacronym.append(thing)

    message = "".join(newacronym).upper()
        
    print(message)



main()
