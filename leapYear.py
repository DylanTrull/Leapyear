# Dylan Trull
# 4/11/2021
# to run this program in terminal type python3 leapYear.py
# input: year(int)
# output: input is a leap year, input is not leap year


def leapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(year, "is a leap year!")
                return True
            else:
                print(year, "is NOT a leap year.")
                return False
        else:
            print(year, "is a leap year!")
            return True
    else:
        print(year, "is NOT a leap year.")
        return False
