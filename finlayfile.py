"""circle - Finlay
triangle - Finlay
volume triangular prism - Finlay
compound interest w/ reacuring input - Finlay
loan with compound interest interest and reacurring payment - Last person
Best price calculator - Finlay
Escape velocity calculator - Finlay"""

"""Template: 
    import math
    import os
    import time
    val = False
    while val == False:
        print("-------------------------\nPlease make a selection\n-------------------------")
        try:
            choice = int(input('To solve for radius type "1" for radius \nTo solve for circumference type "2"\nTo solve for area type "3"\n'))
            time.sleep(1)
            os.system('cls')
            if choice in range(1,4):
                val = True
            else: 
                print("You entered an invalid input")
        except:
            print("You entered an invalid input")
            time.sleep(1)
            os.system('cls')
            val = False
"""

def circle():
    import math
    import os
    import time
    val = False
    while val == False:
        print("-------------------------\nPlease make a selection\n-------------------------")
        try:
            choice = int(input('To solve for radius type "1" for radius \nTo solve for circumference type "2"\nTo solve for area type "3"\n'))
            time.sleep(1)
            os.system('cls')
            if choice in range(1,4):
                val = True
            else: 
                print("You entered an invalid input")
        except:
            print("You entered an invalid input")
            time.sleep(1)
            os.system('cls')
            val = False
    if choice == 1:
        a = float(input("Please enter the area of the circle: "))
        r = (a / math.pi)**0.5
        r = round(r,2)
        print(f"The answer is {r}")
        return a
    elif choice == 2:
        r = float(input("Please enter the radius of the circle: "))
        C = 2*math.pi*r
        C = round(C,2)
        print(f"The answer is {C}")
        return C
    elif choice == 3:
        r = float(input("Enter radius of the circle"))
        A = math.pi*r**2
        A = round(A,2)
        print(f"The answer is {A}")
        return A
    




if __name__ == "__main__":
    circle()