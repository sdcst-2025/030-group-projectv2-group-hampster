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






import lucasfile
import lucasfile as l



print("*list of calculators*")
print("0)instructions")
print("1)rectangle calculator")
print("2)calculator")
print("3)calculator")
print("2)calculator")
print("3)calculator")
print("2)calculator")
print("3)calculator")
print("2)calculator")
print("3)calculator")
print("2)calculator")
print("3)calculator")
print("2)calculator")
print("3)calculator")

choice=input('Enter a choice of calculator: ')
    

if choice=='1':
      print("instructions: enter one of the numbers listed to relocate to that calculator, or to exit.\n The calculator will not work if you enter an invalid number\n...")
if choice=='2':
      l.rectangle()
'''if choice=='3':
        volume of a sphere(lucas)
if choice=='4':
        area of a circle (finlay)
if choice=='5':
        
if choice=='6':
        
if choice=='7':
        
if choice=='8':
        
if choice=='9':
        
if choice=='10':
        
if choice=='11':
        
if choice=='12':
        
if choice=='13':
'''       
if choice=='14':
          exit()


#create a loan with compound interest and reacurring payment
p = int(input("Enter the principal amount: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter time in years: " ))

def compound_intrest(p,r,t):
        Amount = p * (pow((1 + r / 100), t))
        CI = Amount - p
        print("Compound interest is", CI)

