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
            choice = int(input('To solve for radius type "1" \nTo solve for circumference type "2"\nTo solve for area type "3"\n'))
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
#1
def circle(R):
    import math
    import os
    import time
    os.system('cls')
    val = False
    while val == False:
        print("-------------------------\nPlease make a selection\n-------------------------")
        try:
            choice = int(input('To solve for radius type "1"\nTo solve for circumference type "2"\nTo solve for area type "3"\n'))
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
        shape = False
        while shape == False:
            try:
                a = float(input("Please enter the area of the circle: "))
            except:
                print("Please enter a valid input")
                time.sleep(1)
                os.system('cls')
                continue
            if A <= 0:
                print("That shape does not exist on the simple plain")
                time.sleep(1)
                os.system('cls')
                continue
            else:
                shape = True
        r = (a / math.pi)**0.5
        r = round(r,R)
        print(f"The answer is {r}")
        return a
    elif choice == 2:
        shape = False
        while shape == False:
            try:
                r = float(input("Please enter the radius of the circle: "))
            except:
                print("Please enter a valid input")
                time.sleep(1)
                os.system('cls')
                continue
            if r <= 0:
                print("That shape does not exist on the simple plain")
                time.sleep(1)
                os.system('cls')
                continue
        C = 2*math.pi*r
        C = round(C,R)
        print(f"The answer is {C}")
        return C
    elif choice == 3:
        shape = False
        while shape == False:
            try:
                r = float(input("Enter radius of the circle"))
            except:
                print("Please enter a valid input")
                time.sleep(1)
                os.system('cls')
                continue
            if r <= 0:
                print("That shape does not exist on the simple plain")
                time.sleep(1)
                os.system('cls')
                continue
        A = math.pi*r**2
        A = round(A,R)
        print(f"The answer is {A}")
        return A
    
#2
def triangle(R):
    import math
    import os
    import time
    os.system('cls')
    val = False
    while val == False:
        print("-------------------------\nPlease make a selection\n-------------------------")
        try:
            choice = int(input('To solve for height type "1" \n To solve for base type "2" \nTo solve for area type "3"\n'))
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
        shape = False
        while shape == False:
            try:
                A = float(input("Please enter the area of the triangle: "))
                b = float(input("Please enter the base of the triangle: "))
            except:
                print("Please enter a valid input")
                time.sleep(1)
                os.system('cls')
                continue
            if A <= 0 or b <= 0:
                print("That shape does not exist on the simple plain")
                time.sleep(1)
                os.system('cls')
                continue
            else:
                shape = True  
        h = 2*A/b
        h = round(h,R)
        print(f"The answer is {h}")
        return h
    elif choice == 2:
        shape = False
        while shape == False:
            try:
                A = float(input("Please enter the area of the triangle: "))
                h = float(input("Please enter the height of the triangle: "))
            except:
                print("Please enter a valid input")
                time.sleep(1)
                os.system('cls')
                continue
            if A <= 0 or h <= 0:
                print("That shape does not exist on the simple plain")
                time.sleep(1)
                os.system('cls')
                continue
            else:
                shape = True
        b = 2*A/h
        b= round(b,R)
        print(f"The answer is {b}")
        return b
    elif choice == 3:
        shape = False
        while shape == False:
            try:
                b = float(input("Please enter the base of the triangle: "))
                h = float(input("Please enter the height of the triangle: "))
            except:
                print("Please enter a valid input")
                time.sleep(1)
                os.system('cls')
                continue
            if b <= 0 or h <= 0:
                print("That shape does not exist on the simple plain")
                time.sleep(1)
                os.system('cls')
                continue
            else:
                shape = True
        A = b*h/2
        A = round(A,R)
        print(f"The answer is {A}")
        return A
#3
def triangularprism(R):
    import math
    import os
    import time
    os.system('cls')
    val = False
    while val == False:
        print("-------------------------\nPlease make a selection\n-------------------------")
        try:
            choice = int(input('To solve for height type "1" \nTo solve for surface area type "2"\nTo solve for volume type "3"\n'))
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
            shape = False
            while shape == False:
                try:
                    a = float(input("Please enter the first base of the triangular prism: "))
                    b = float(input("Please enter the second base of the triangular prism: "))
                    c = float(input("Please enter the third base of the triangular prism: "))
                    V = float(input("Please enter the volume of the triangular prism: "))
                except:
                    print("Please enter a valid input")
                    time.sleep(1)
                    os.system('cls')
                    continue
                if a <= 0 or b <= 0 or c <= 0 or V <= 0:
                    print("That shape does not exist on the simple plain")
                    time.sleep(1)
                    os.system('cls')
                    continue
                else:
                    shape = True
            A = (4*V)/(((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))**0.5)
            A = round(A,R)
            print(f"The answer is {A}")
            return A
        if choice == 2:
            shape = False
            while shape == False:
                try:
                    a = float(input("Please enter the first base of the triangular prism: "))
                    b = float(input("Please enter the second base of the triangular prism: "))
                    c = float(input("Please enter the third base of the triangular prism: "))
                    h = float(input("Please enter the height of the triangular prism: "))
                except:
                    print("Please enter a valid input")
                    time.sleep(1)
                    os.system('cls')
                    continue
                if a <= 0 or b <= 0 or c <= 0 or h <= 0:
                    print("That shape does not exist on the simple plain")
                    time.sleep(1)
                    os.system('cls')
                    continue
                else:
                    shape = True
            s = (a + b + c)/2
            ab = (s*(s-a)*(s-b)*(s-c))**0.5
            A = 2*ab + (a+b+c)*h
            A = round(A,R)
            print(f"The answer is {A}")
            return A
        if choice == 3: 
            shape = False
            while shape == False:
                try:
                    a = float(input("Please enter the first base of the triangular prism: "))
                    b = float(input("Please enter the second base of the triangular prism: "))
                    c = float(input("Please enter the third base of the triangular prism: "))
                    h = float(input("Please enter the height of the triangular prism: "))
                except:
                    print("Please enter a valid input")
                    time.sleep(1)
                    os.system('cls')
                    continue
                if a <= 0 or b <= 0 or c <= 0 or h <= 0:
                    print("That shape does not exist on the simple plain")
                    time.sleep(1)
                    os.system('cls')
                    continue
                else:
                    shape = True
            V = (h/4)*((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))**0.5
            V = round(V,R)
            print(f"The answer is {V}")
            return V
#4
def compoundinterest():
    import math
    import os
    import time
    val = False
    while val == False:
        print("-------------------------\nPlease make a selection\n-------------------------")
        try:
            choice = int(input('To solve for compound interest on a fixed deposit type "1"\nTo solve for compound interest on a reaccuring deposit type "2"\n'))
            time.sleep(1)
            os.system('cls')
            if choice in range(1,3):
                val = True
            else: 
                print("You entered an invalid input")
        except:
            print("You entered an invalid input")
            time.sleep(1)
            os.system('cls')
            val = False
    if choice == 1:
        shape = False
        while shape == False:
            try:
                P = float(input("Please enter the deposited amount: "))
                r = float(input("Please enter the interest rate: "))
                n = float(input("Please enter the compounding rate: "))
                t = float(input("Please enter the time in years: "))
            except:
                print("Please enter a valid input")
                time.sleep(1)
                os.system('cls')
                continue
            if P <= 0 or r <= 0 or n <= 0:
                print("All values excluding time must be greater than 0")
                time.sleep(1)
                os.system('cls')
                continue
            else:
                shape = True
        A = P*(1+(r/n))**(n*t)
        A = round(A,2)
        print(f"The answer is ${A}")
        return A
    if choice == 2:
        shape = False
        while shape == False:
            try:
                P = float(input("Please enter the deposited amount: "))
                r = float(input("Please enter the interest rate: "))
                n = float(input("Please enter the number of compounds per year: "))
                t = float(input("Please enter the time in years: "))
                cr = float(input("Please enter the number of reaccuring contributions per year"))
                ca = float(input("Please enter the reaccurring contribution amount"))
            except:
                print("Please enter a valid input")
                time.sleep(1)
                os.system('cls')
                continue
            if P <= 0 or r <= 0 or n <= 0 or cr <= 0 or ca <= 0:
                print("All values excluding time must be greater than 0")
                time.sleep(1)
                os.system('cls')
                continue
            else:
                shape = True
            c = int(cr*t)
            for i in range(c+1):
                

if  __name__ == "__main__":
    R = 2
    compoundinterest() 