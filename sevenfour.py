


def main():

    creditsearned = int(input("How many credit hours have you earned?:"))
    if creditsearned < 7:
        print("You are a freshman!")
    if creditsearned >= 7 and creditsearned < 16:
        print("You are a sophomore!")
    if creditsearned >= 16 and creditsearned < 26:
        print("You are a junior!")
    if creditsearned > 26:
        print("You are a senior!")
    
    











main()
