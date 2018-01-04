# lottery for python v0.01

import random
import sys
import time
print("\nWelcome to the trashy lottery \n")

try:
    while True:
        try:
            lower_limit = int(input("Enter the lower limit for the draw: "))
        except ValueError:
            print("Opps, please enter a valid number.")
            continue
        else:
            break
    while True:
        try:
            upper_limit = int(input("Enter the upper limit for the draw: "))
            if upper_limit < lower_limit:
                print("The number must be greater or equal to the lower limit!")
                continue
        except ValueError:
            print("Opps, please enter a valid number.")
            continue
        else:
            break

    print("Now we'll pick a number! ")
    for i in range(101):
        time.sleep(0.015)
        sys.stdout.write("\r%d%%" % i)
        randpick = random.randint(lower_limit, upper_limit)
        if i == 100:
            print()

    while True:
        try:
            pick = int(input("Now you get to pick a number! "))
            if pick < lower_limit or pick > upper_limit:
                print("Your pick must be between the lower and the upper limit!")
                continue
        except ValueError:
            print("Opps, please enter a valid number:")
            continue
        else:
            break
    print("Alright now, lets see what you got! ")
    if randpick == pick:
        print("You won!!!!!")
    else:
        print("Though luck :( but try again!")
except KeyboardInterrupt:
    print("\nSorry to see you go so soon! M#$!@$F#@*$^")
