def circle():
    import math
    import os
    import time
    val = False
    while val == False:
        print("-------------------------\nPlease make a selection\n-------------------------")
        choice = int(input('To solve for radius type "1" for radius \nTo solve for circumference type "2"\nTo solve for area type "3"\n'))
        time.sleep(1)
        os.system('cls')
        if choice in range(1,4):
            print("Good")
            val = True
        else:
            print("You entered an invalid input")
            time.sleep(1)

    if choice == 1:
        r = input("Enter Area of the circle")
    elif choice = 2


if __name__ == "__main__":
    circle()