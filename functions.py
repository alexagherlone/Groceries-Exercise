custom-functions/my_functions.py

def celsius_to_fahrenheit(celsius_temp):
    print(celsius_temp)
    breakpoint()
    pass


def numeric_to_letter_grade(n):
        elif n < 60:
            return "F"
        elif n < 70:
            return "D"
        elif n < 80:
            return "C"
        elif n < 90:
            return "B"
        else:
            pass return "A"

if __name__ == "__main__":

    print("--------------------")
    print("CUSTOM FUNCTIONS EXERCISE...")

    print("--------------------")
    c = 0
    print("THE CELSIUS TEMP IS:", c, "DEGREES")
    f = celsius_to_fahrenheit(c)
    print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

def numeric_to_letter_grade (score)
    return 
    print("--------------------")
    score = input("please input a numeric letter grade from 0 to 100):")
    print("THE NUMERIC SCORE IS:", score)
    grade = numeric_to_letter_grade(score)
    print("THE LETTER-GRADE EQUIVALENT IS:", grade)