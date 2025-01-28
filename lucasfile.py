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
            else:
                print(' ')
        except:
            print('You didn\'t select an option.')
        
    os.system('cls')






if __name__ == "__main__":
    rectangle()