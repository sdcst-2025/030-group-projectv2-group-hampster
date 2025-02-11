# creating a menu
#first get the input number for that calculator you want and add a way to prevent wrong numbers, then add all the calculators to the menu and make it so you can select them. Lastly make the menu look good by adding things to it.
import os,math

def colored_text(text, text_color=37, bg_color=40):
    
    print(f"\033[{text_color}m\033[{bg_color}m{text}\033[0m")

text_colors = {
    "black": 30, "red": 31, "green": 32, "yellow": 33, 
    "blue": 34, "magenta": 35, "cyan": 36, "white": 37
}

bg_colors = {
    "black": 40, "red": 41, "green": 42, "yellow": 43, 
    "blue": 44, "magenta": 45, "cyan": 46, "white": 47
}


def title():
        colored_text("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", text_colors["white"], bg_colors["red"])
        colored_text("@@@@@@       @       @@       @      @@      @@@@@@@@@       @@      @@@   @@@      @@       @@@@@@@", text_colors["white"], bg_colors["red"])
        colored_text("@@@@@@  @@@@ @  @@@  @@      @@     @@%     @@@@@@@@@@:     @@@      @@:   %@@      @@       @@@@@@@", text_colors["white"], bg_colors["red"])
        colored_text("@@@@@@@ @@@@ @@ @@@   @  @@@@@  @@@@@@  @@@@@@@@@@@@@@  @@@@@@@@@  @@@  @@@  @ @@@@  @@@@ .@@@@@@@@@", text_colors["white"], bg_colors["red"])
        colored_text("@@@@@@@      @@    @@@@       @@@@@  @@@@@@  *@@@@@@@@@@@@@  %@@@  @@@       @     @@@@@@  @@@@@@@@@", text_colors["white"], bg_colors["red"])
        colored_text("@@@@@@   @@@@@  @@    @  @@@@@@     @@@     @@@@@@@@@@=     @@@@@  @@@  @@@  @  @@   @@@@  @@@@@@@@@", text_colors["white"], bg_colors["red"])
        colored_text("@@@@@@   @@@@@   @    @       @     @@@      @@@@@@@@@      @@@@@  @@@  @@@  @   @@   @@@  @@@@@@@@@", text_colors["white"], bg_colors["red"])
        colored_text("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", text_colors["white"], bg_colors["red"])

title()

input("")
os.system('cls')

import finlayfile as f
import lucasfile as l


print("*list of calculators*")
print("1)Instructions")
print("2)Rectangle calculator")
print("3)Volume of sphere calculator")
print("4)Circle calculator")
print("5)Triangle calculator")
print("6)Simple interest calculator")
print("7)Triangular prism calculator")
print("8)Cylinder calculator")
print("9)Rectangular prism claculator")
print("10)Escape velocity calculator")
print("11)Bullet energy calculator")
print("12)Compound interest calculator")
print("13)Best price calculator")
print("14)flip a coin")
print("15)random number generator")
print("16)Exit")

choice=input('Enter a choice of calculator: ')
if choice == "16":
       exit()
R = int(input('How many decimal points do you want to round to? '))
if choice in ['']:
        R = int(input('How many decimal points do you want to round to? '))

def rounded_value():
    try:
        rnum = int(input("How many decimal places do you want? "))
        if rnum < 0:
            print("Decimal places cannot be negative.")
            return None
        R = round(R, rnum)
        return R
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        return None




if choice=='1':
      print("instructions: enter one of the numbers listed to relocate to that calculator, or to exit.\n The calculator will not work if you enter an invalid number\n...")
if choice=='2':
        l.rectangle(R)
if choice=='3':
        l.volsphere(R)
if choice=='4':
        f.circle(R)
if choice=='5':
        f.triangle(R)
if choice=='6':
        l.simpleinterest()
if choice=='7':
        f.triangularprism(R)
if choice=='8':
        l.cylinder(R)
if choice=='9':
        l.rectangularprism(R)
if choice=='10':
        f.escapevelocity(R)
if choice=='11':
        l.bullet(R)
if choice=='12':
        f.compoundinterest
if choice=='13':
        f.bestprice
if choice=='14':
        l.coin
if choice=='15':
        l.randomnumber
if choice=='16':
       exit()