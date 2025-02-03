# creating a menu
#first get the input number for that calculator you want and add a way to prevent wrong numbers, then add all the calculators to the menu and make it so you can select them. Lastly make the menu look good by adding things to it.
import os

print("start calculating")


print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("@@@@@@       @       @@      @@     @@%     @@@@@@@@@@:     @@@      @@:   %@@      @@*      @@@@@@@")
print("@@@@@@@ @@@@ @@ @@@   @  @@@@@  @@@@@@  @@@@@@@@@@@@@@  @@@@@@@@@  @@@  @@@  @ @@@@  @@@@ .@@@@@@@@@")
print("@@@@@@@      @@    @@@@  @@@@@@@@@@  @@@@@@  *@@@@@@@@@@@@@  %@@@  @@@       @     @@@@@@  @@@@@@@@@")
print("@@@@@@  :@@@@@  @@    @       @     @@@     @@@@@@@@@@=     @@@@@  @@@  @@@  @  @@   @@@@  @@@@@@@@@")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")



input("")
os.system('cls')


import finlayfile as f
import lucasfile as l



print("*list of calculators*")
print("1)instructions")
print("2)rectangle calculator")
print("3)volume of sphere calculator")
print("4)circle calculator")
print("5)triangle calculator")
print("6)simple interest calculator")
print("7)triangular prism calculator")
print("8)cylinder calculator")
print("9)calculator")
print("10)calculator")
print("11)calculator")
print("12)calculator")
print("13)calculator")
print("14)calculator")

choice=input('Enter a choice of calculator: ')
rnum = int(input('how many decimal places do you want? '))

def get_rounded_value():
    try:
        rnum = int(input("How many decimal places do you want? "))
        if rnum < 0:
            print("Decimal places cannot be negative.")
            return None
        R = round(1, rnum)
        return R
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
        return None




if choice=='1':
      print("instructions: enter one of the numbers listed to relocate to that calculator, or to exit.\n The calculator will not work if you enter an invalid number\n...")
if choice=='2':
        l.rectangle()
if choice=='3':
        l.volsphere()
if choice=='4':
        f.circle()
if choice=='5':
        f.triangle()
if choice=='6':
        l.simpleinterest()
if choice=='7':
        f.triangularprism()
if choice=='8':
        l.cylinder()
'''if choice=='9':
        
if choice=='10':
        
if choice=='11':
        
if choice=='12':
        
if choice=='13':

if choice=='14':
       exit()
'''



