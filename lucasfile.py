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
    basic derivative calculator - Lucas
    Best price calculator - Finlay
    Gravitation time dilation calculator - Lucas
    Escape velocity calculator - Finlay
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
        s1 = float(input("Enter the given side: "))
        area = float(input("Enter the area: "))
        ans = area/s1
    if choice == 2:
        s1 = float(input("Enter first side: "))
        s2 = float(input("Enter second side: "))
        ans = (s1*2)+(s2*2)
    if choice == 3:
        s1 = float(input("Enter first side: "))
        s2 = float(input("Enter second side: "))
        ans = s1*s2
    os.system('cls')
    ans = round(ans, 2)
    print(f"The answer is {ans}.")
    return

def volsphere()
if __name__ == "__main__":
