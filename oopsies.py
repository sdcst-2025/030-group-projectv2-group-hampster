os.system('cls')
    picked = 0
    picked1 = 0
    while picked == 0:
        os.system('cls')
        print("-------------------------\nSimple Interest Calculator\n-------------------------")
        try:
            p = float(input("Enter the amount of money: "))
            r = float(input("Enter the interest rate: "))
            t = float(input("Enter the amount of years: "))
            if p > 0 and r > 0 and t >= 0:
                picked = 1
            else: 
                print("You didn't enter a valid input.")
        except:
            print("You didn't enter a valid input.")
    print('-------------------------\nSelect Compound Period\n-------------------------')
    print('For every second,    type "1"')
    print('For every minute,    type "2"')
    print('For every hour,      type "3"')
    print('For semidaily,       type "4"')
    print('For daily,           type "5"')
    print('For semiweekly,      type "6"')
    print('For weekly,          type "7"')
    print('For biweekly,        type "8"')
    print('For semimonthly,     type "9"')
    print('For monthly,         type "10"')
    print('For bimonthly,       type "11"')
    print('For semiannualy,     type "12"')
    print('For annually,        type "13"')
    print('For every decade,    type "14"')
    print('For every century,   type "15"')
    print('For every millennia, type "16"')
    while picked1 == 0:
        try:
            period = int(input(""))
            if 0 < period < 17:
                picked1 = 1
            else:
                print("You didn't enter a valid input.")
        except:
            print("You didn't enter a valid input.")
    



    ans = round(ans, 2)
    print(f"The answer is {ans}.")
    return