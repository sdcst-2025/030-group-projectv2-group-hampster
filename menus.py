import os
import math
import finlayfile as f
import lucasfile as l
import wimfile as w

def colored_text(text, text_color=30, bg_color=37):
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
    colored_text("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", text_colors["white"], bg_colors["red"])
    colored_text("@@@@@@       @       @@       @@     @@@      @@@@@@@@       @@    @@   @@@      @@        @@        @@", text_colors["white"], bg_colors["red"])
    colored_text("@@@@@@  @@@@ @  @@@  @@       @@     @@%     @@@@@@@@@      @@@    @@   @@@      @2        @@   @@   @@", text_colors["white"], bg_colors["red"])
    colored_text("@@@@@@@ @@@@ @@ @@@   @  @@@@@@  @@@@@@  @@@@@@@@@@@@@  @@@@@@@  @  @   @@@@@  @@@@    @@@@@@   @@   @@", text_colors["white"], bg_colors["red"])
    colored_text("@@@@@@@      @@    @@@@       @@@@@  @@@@@@  *@@@@@@@@      %@@  @@  @  @@@@@  @@@@        @@       @@@", text_colors["white"], bg_colors["red"])
    colored_text("@@@@@@   @@@@@  @@    @  @@@@@@     @@@     @@@@@@@@@@  @@@@@@@  @@@    @@@@@  @@@@    @@@@@@   @@   @@", text_colors["white"], bg_colors["red"])
    colored_text("@@@@@@   @@@@@   @    @       @     @@@      @@@@@@@@@      @@@  @@@@   @@@@@  @@@@        @@   @@   @@", text_colors["white"], bg_colors["red"])
    colored_text("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", text_colors["white"], bg_colors["red"])
title()

input("")
os.system('cls')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("*List of calculators*")
        print("1) Instructions")
        print("2) Rectangle calculator")
        print("3) Volume of sphere calculator")
        print("4) Circle calculator")
        print("5) Triangle calculator")
        print("6) Simple interest calculator")
        print("7) Triangular prism calculator")
        print("8) Cylinder calculator")
        print("9) Rectangular prism calculator")
        print("10) Escape velocity calculator")
        print("11) Bullet energy calculator")
        print("12) Compound interest calculator")
        print("13) Best price calculator")
        print("14) Flip a coin")
        print("15) Random number generator")
        print("16) Exit")
        
        choice = input("Enter a choice of calculator: ")
        
        if choice == "16":
            print("Exiting program")
            break
        
        if choice in ['2', '3', '4', '5', '7', '8', '9', '10', '11']:
            try:
                R = int(input("How many decimal points do you want to round to? "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
        
        if choice == '1':
            print("Instructions: Enter one of the numbers listed to use that calculator, or select exit to quit.")
        elif choice == '2':
            l.rectangle(R)
        elif choice == '3':
            l.volsphere(R)
        elif choice == '4':
            f.circle(R)
        elif choice == '5':
            f.triangle(R)
        elif choice == '6':
            l.simpleinterest()
        elif choice == '7':
            f.triangularprism(R)
        elif choice == '8':
            l.cylinder(R)
        elif choice == '9':
            l.rectangularprism(R)
        elif choice == '10':
            f.escapevelocity(R)
        elif choice == '11':
            l.bullet(R)
        elif choice == '12':
            f.compoundinterest()
        elif choice == '13':
            f.bestprice()
        elif choice == '14':
            l.coin()
        elif choice == '15':
            l.randomnumber()
        elif choice == '17':
            w.adventure()
        
        else:
            print("Invalid choice. Please enter a valid number.")
        input("Press Enter to go back to menu.")
        
if __name__ == "__main__":
    main()


