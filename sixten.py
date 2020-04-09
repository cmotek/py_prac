


def main():
    phrase = input("Give me your acronym phrase:")

    def acronym(phrase):
        newacronym = []
        for i in phrase.split():
            capitalizer = i[0]
            newacronym.append(capitalizer)

        message = "".join(newacronym).upper()
        return message

    print(acronym(phrase))


main()
