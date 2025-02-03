'''
List of calculators:
    circle - Finlay
    rectangle - Lucas
    triangle - Finlay
    volume sphere - Lucas
    volume triangular prism - Finlay
    volume rectangular prism - Lucas
    compound interest w/ reacuring input - Finlay
    simple interest with reacurring input - Lucas
    loan with compound interest interest and reacurring payment - Last person
    Best price calculator - Finlay
    Gravitation time dilation calculator - Lucas
    Escape velocity calculator - Finlay
    cylinder - Lucas
    '''
import os, math

def rectangle():
    os.system('cls')
    picked = 0
    while picked == 0:
        print('-------------------------\nPlease make a selection: \n-------------------------')
        print('To solve for a missing side length, type "1"')
        print('To solve for the perimeter, type "2"')
        print('To solve for the area, type "3"')
        try:
            choice = int(input(""))
            if choice > 0 and choice < 4:
                picked = 1
                os.system('cls')
            else:
                os.system('cls')
                print('You didn\'t select an option.')
        except:
            os.system('cls')
            print('You didn\'t select an option.')
    if choice == 1:
        s1 = float(input("Enter the given side length: "))
        area = float(input("Enter the area: "))
        ans = area/s1
    if choice == 2:
        s1 = float(input("Enter the first side length: "))
        s2 = float(input("Enter the second side length: "))
        ans = (s1*2)+(s2*2)
    if choice == 3:
        s1 = float(input("Enter the first side length: "))
        s2 = float(input("Enter the second side length: "))
        ans = s1*s2
    os.system('cls')
    ans = round(ans, R)
    print(f"The answer is {ans}.")
    return

def volsphere():
    os.system('cls')
    picked = 0
    while picked == 0:
        print('-------------------------\nPlease make a selection: \n-------------------------')
        print('To solve for the radius, type "1"')
        print('To solve for the surface area, type "2"')
        print('To solve for the volume, type "3"')
        try:
            choice = int(input(""))
            if choice > 0 and choice < 4:
                picked = 1
                os.system('cls')
            else:
                os.system('cls')
                print('You didn\'t select an option.')
        except:
            os.system('cls')
            print('You didn\'t select an option.')
    if choice == 1:
        vol = float(input("Enter the volume: "))
        ans = (3*(vol/(4*math.pi)))**(1/3)
    if choice == 2:
        rad = float(input("Enter the radius: "))
        ans = (4*math.pi*(rad**2))
    if choice == 3:
        rad = float(input("Enter the radius: "))
        ans = ((4/3)*math.pi*(rad**3))
    os.system('cls')
    ans = round(ans, R)
    print(f"The answer is {ans}.")
    return

def rectangularprism():
    os.system('cls')
    picked = 0
    while picked == 0:
        print('-------------------------\nPlease make a selection: \n-------------------------')
        print('To solve for the missing side length, type "1"')
        print('To solve for the surface area, type "2"')
        print('To solve for the volume, type "3"')
        try:
            choice = int(input(""))
            if choice > 0 and choice < 4:
                picked = 1
                os.system('cls')
            else:
                os.system('cls')
                print('You didn\'t select an option.')
        except:
            os.system('cls')
            print('You didn\'t select an option.')
    if choice == 1:
        s1 = float(input("Enter the first side length: "))
        s2 = float(input("Enter the second side length: "))
        vol = float(input("Enter the volume: "))
        ans = vol/s1/s2
    if choice == 2:
        l = float(input("Enter the length: "))
        w = float(input("Enter the width: "))
        h = float(input("Enter the height: "))
        ans = 2*((w*l)+(h*l)+(h*w))
    if choice == 3:
        l = float(input("Enter the length: "))
        w = float(input("Enter the width: "))
        h = float(input("Enter the height: "))
        ans = l*w*h
    os.system('cls')
    ans = round(ans, R)
    print(f"The answer is {ans}.")
    return

def cylinder():
    os.system('cls')
    picked = 0
    while picked == 0:
        print('-------------------------\nPlease make a selection: \n-------------------------')
        print('To solve for the radius, type "1"')
        print('To solve for the surface area, type "2"')
        print('To solve for the volume, type "3"')
        try:
            choice = int(input(""))
            if choice > 0 and choice < 4:
                picked = 1
                os.system('cls')
            else:
                os.system('cls')
                print('You didn\'t select an option.')
        except:
            os.system('cls')
            print('You didn\'t select an option.')
    if choice == 1:
        h = float(input('Enter the height: '))
        v = float(input('Enter the volume: '))
        ans = (v/(math.pi*h))**(1/2)
    if choice == 2:
        r = float(input('Enter the radius: '))
        h = float(input('Enter the height: '))
        ans = (2*math.pi*r*h+2*math.pi*(r**2))
    if choice == 3:
        r = float(input('Enter the radius: '))
        h = float(input('Enter the height: '))
        ans = math.pi*(r**2)*h
    os.system('cls')
    ans = round(ans, R)
    print(f"The answer is {ans}.")
    return

def simpleinterest():
    os.system('cls')
    picked = 0
    picked1 = 0
    while picked == 0:
        os.system('cls')
        print("-------------------------\nSimple Interest Calculator\n-------------------------")
        try:
            p = float(input("Enter the amount of money: "))
            r = float(input("Enter the interest rate in percent (%): "))
            t = float(input("Enter the amount of years: "))
            if p > 0 and r > 0 and t >= 0:
                picked = 1
            else: 
                print("You didn't enter a valid input.")
        except:
            print("You didn't enter a valid input.")
    ans = p*(r/100)*t
    ans = round(ans, 2)
    print(f"The answer is ${ans}.")
    return

#one more calc, not grav



if __name__ == "__main__":
    simpleinterest()


'''
TEMPLATE FOR FUNCTIONS:


    os.system('cls')
    picked = 0
    while picked == 0:
        print('-------------------------\nPlease make a selection: \n-------------------------')
        print('To solve for the , type "1"')
        print('To solve for the , type "2"')
        print('To solve for the , type "3"')
        try:
            choice = int(input(""))
            if choice > 0 and choice < 4:
                picked = 1
                os.system('cls')
            else:
                os.system('cls')
                print('You didn\'t select an option.')
        except:
            os.system('cls')
            print('You didn\'t select an option.')
    if choice == 1:
        pass
    if choice == 2:
        pass
    if choice == 3:
        pass
    os.system('cls')
    ans = round(ans, 2)
    print(f"The answer is {ans}.")
    return



'''