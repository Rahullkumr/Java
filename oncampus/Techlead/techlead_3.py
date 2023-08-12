# 3. Write a program to check if a given year is a leap year.
# Leap Year: a year divisible by 4 but not by 100 until also divisible by 400

def is_leap(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
        else:
            return True
    else:
        return False

year = int(input("Enter year: "))
if year < 0:
    print("Enter valid year")
else:
    if is_leap(year):
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")