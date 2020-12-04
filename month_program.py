#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program can display the month of the year that represents that number


def main():
    # this function can convert integers into months

    print("This program can display the month of the year that"
          " represents that number")

    # input
    month_number = int(input("Enter a number of a month: "))
    print("")

    # process & output
    if month_number == 1:
        print("January")
    elif month_number == 2:
        print("February")
    elif month_number == 3:
        print("March")
    elif month_number == 4:
        print("April")
    elif month_number == 5:
        print("May")
    elif month_number == 6:
        print("June")
    elif month_number == 7:
        print("July")
    elif month_number == 8:
        print("August")
    elif month_number == 9:
        print("September")
    elif month_number == 10:
        print("October")
    elif month_number == 11:
        print("November")
    elif month_number == 12:
        print("December")
    else:
        print("{} is not a month!".format(month_number))


if __name__ == "__main__":
    main()
