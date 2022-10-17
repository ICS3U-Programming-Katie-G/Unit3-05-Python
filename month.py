#!/usr/bin/env python3
# Created by: Katie G
# Created on: October 17th, 2022
# This program gets an integer from 1
# to 12, which represents a month.
# The corresponding month is displayed
# back to the user.

# This function checks the user int
# to see which month the number
# corresponds to. Since there is no
# switch case in Python, this function
# will be the replacement for one.
# The corresponding month will then
# be displayed to the user.
def find_month(month):
    months = {
        1: "Number {} corresponds to January!".format(month),
        2: "Number {} corresponds to February!".format(month),
        3: "Number {} corresponds to March!".format(month),
        4: "Number {} corresponds to April!".format(month),
        5: "Number {} corresponds to May!".format(month),
        6: "Number {} corresponds to June!".format(month),
        7: "Number {} corresponds to July!".format(month),
        8: "Number {} corresponds to August!".format(month),
        9: "Number {} corresponds to September!".format(month),
        10: "Number {} corresponds to October!".format(month),
        11: "Number {} corresponds to November!".format(month),
        12: "Number {} corresponds to December!".format(month),
    }
    return months.get(month, "{} is not a valid input.".format(month))


if __name__ == "__main__":
    user_month_num = int(input("Hi! Enter a number between 1-12,get the corresponding month! ")
    )
    print(find_month(user_month_num))
