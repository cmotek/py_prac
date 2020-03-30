


def main():
    grade = int(input("Input your grade:" ))
    grades = ["F", "D", "C", "B", "A"]
    newgrade = 0
    if grade >= 90:
        newgrade = 4
    elif grade >= 80 and grade < 90:
        newgrade = 3
    elif grade >= 70 and grade < 80:
        newgrade = 2
    elif grade >= 60 and grade < 70:
        newgrade = 1
    else:
        newgrade = 0

    print(grades[newgrade])
        













main()
