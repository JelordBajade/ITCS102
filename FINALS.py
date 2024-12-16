def main():
    while True:
        print("")
def act_1():
    print("Hello World")
def act_2():
    name = input ("jelord")

    print ("Hi" + name )
def act_3():
    name = input("Please input your name here ---> ")
    fname = input("Please input your fname here ---> ")
    mname = input("Please input your mname here ---> ")
    birthdate = input("Please input your birth date here ---> ")
    birthmonth = input("Please input your birthmonth here ---> ")
    birthyear = input("Please input your birthyear here ---> ")
    maritalstatus = input("Please input your maritalstatus here ---> ")
    religion = input("Please input your religion here ---> ")
    ethnicity = input("Please input your ethnicity here ---> ")
    mobile = input("Please input your mobile here ---> ")
    email = input("Please input your email here ---> ")
    gender = input("Please input your gender here ---> ")
    address = input("Please input your address here ---> ")
    age = input(" Please input your age here ---> ")


    print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")

def act_4():
    number1 = eval(input("please type number--->"))
    number2 = eval(input("please type number--->"))

    answer	= number1 + number2
    print ("the sum of", number1, "and" , number2, "is" ,answer)
def act_5():
    x = 5

    print (x)

    x = x + 10

    print (x)

    x = x + 15

    print(x)

    x += 10

    print(x)
def act_6():
    Fah = eval(input("enter temperature in Fahrenheit : "))
    celsius = (Fah - 32) * 5 / 9

    print (" the comversion of" , Fah , "degrees fahrenheit is" , celsius , "degrees celsius")

    print (F" the comversion of {Fah} degrees fahrenheit is {round(celsius,2)} degrees celsius")

def act_7():
    gold = 0

    miner = input("Enter Name")

    hasmine = input("Did you mine gold today ?")

    if hasmine.lower() == "yes":
        gold +=1
        print (f"Hi {miner}, today you have a total of {gold} gold ")
    else: 
        print (f"Hi {miner}, today you have a total of {gold} gold ")
def act_8():
    password = input("please enter your password : ")

    if password.lower() == " mahal ko pa sya ":
        print (" congrats ang rupok mo")
        print ("enjoy using the system")
    elif password == "mahal ko pa sya":
        print (" congrats ang rupok mo")
        print ("enjoy using the system")


    else:
        print ("bawal ang marupok")
    print ("thank you for using the system")

def act_9():
    age = eval(input(" enter your age : "))
    if age>= 1 and age <= 7 :
        print ("toddler")
    elif age >= 8 and age <= 13:
        print (" pre teen")
    elif age >= 14 and age <= 18:
        print("Teenager")
    elif age <= 21:
        print("Early Adulthood")
    elif age <= 45:
        print("Mid Adulthood")
    elif age <= 59:
        print("Post Adult")
    elif age >= 60 and age <= 100:
        print("Senior")
    else:
        print("INVALID AGE")
def act_10():
    isDLL= input('Are you a current student of DLL (yes/no):  ')

    if isDLL.lower() == 'yes':
        print('Welcome to the DLL BSIT Scholarship form')
        isCotta= input('Are you from Barangay Cotta (yes/ no):  ')

        if isCotta.lower() == 'yes':
            print('Please fillup the second form')
            isLevel=input('What is your current level right now in DLL\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\nPlease input your answer')
            if isLevel.lower() == 'f':
                print('Hi Freshmen')
            elif isLevel.lower() == 's':
                print('Hi Sophomore')
            elif isLevel.lower() == 'j':
                print('Hi Junior')
            elif isLevel.lower() == 'r':
                print('Hi Senior')
            else:
                print('Invalid choice')
            isNeeded = input('Do you need this scholarship (yes/no):  ')
        
            if isNeeded.lower() == 'yes':
                print('Scholarship Granted')
            else:
                print('Thanks for stopping by')
        else:
            print('Sorry, this Scholarship grant are only for resident of Cotta')

    else:
        print('Thanks for stopping by')
def act_11():
    for me in range (1 , 101):
        print(me, 'GOODBYE WORLD')
def act_12():
    for cycle in range (10,0,-1):
        print(cycle)
def act_13():
    sum = 1
    num=int(input('Enter a number: '))

    for x in range (num,0,-1):
        sum *= x
    print(f"The factorial of {num} is {sum}")
def act_14():
    for x in range ( 0, 11,):
        print(x,end =" ")
    for y in range (0, 11):
        print("*",end = " ")
    print("")
def act_15():
    for x in range ( 0, 11,):
        print(x,end =" ")
    for y in range (0, x):
        print("*",end = " ")
    print("")
def act_16():
    for x in range (1,11,):
        for y in range (1, x + 1):
            print(" ",end=" ")
        for z in range(11, x, -1):
            print(" * ",end=" ")
        print()
def act_17():
    col = eval(input("Enter number of columns---> "))


    for x in range (1, 11):
        for y in range (1, col + 1):
            print(f"{x} x {y} = {x*y}" ,end="\t")
        print()
def act_18():
    tri = eval(input("Enter a number of triangle---> "))

    for x in range (1, 6):
        for r in range (1 , tri + 1):
            for y in range (1 , x + 1):
                print("*", end=" ")
            for z in range (6, x, -1):
                print(" ",end=" ")
        print()
def act_19():
    tuloy = True
    while tuloy == True:
        name = input("Enter your name: ")
        if name.lower()== "stop":
            print("PROGRAM TERMINATED")
            break
            tuloy = False
        else:
            continue
def act_20():
    import os

    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        else:
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
            continue
def act_21():
    def pang_hi():
        print("HI IT1C")

    def pang_hi_v2(name):
        print(f"Hello {name}")

    def termi():
        print("PROGRAM TERMINATED")

    def activity_2():
        number1 = eval (input("enter a number--->" ))
        number2 = eval (input("enter another number--->" ))
        answer = (number1 + number2)
        print(f"The sum of {number1} and {number2} is {answer}")

    tuloy =  True
    while tuloy == True:
        ask = input("Enter a name---> ")

        if ask.lower() != "stop":
            pang_hi_v2(ask)
            if ask == "2":
                activity_2()
                continue
        else:
            termi()
            break

def act_22():
    lup = True
    names = []


    while lup == True:
        askName = input("What name would you like to add?> ")
        if askName.lower() == "stop":
            print(names)
            print(f"You have entered {len(names)} names!")
            break
        else:
            names.append(askName)
def act_23():
    def factorial(factor):
        """This function is for calculating the factorial of a numver that is provided, it will automatically compute the factorial of the provided number."""
        fact = 1
        for x in range(factor, 0, -1):
            fact *= x
            print(fact)
        return fact

    factorial(5)

    help(factorial)
def act_24():
    # from actvity23 import factorial

    # print(f"the factorial of 7 is {factorial(7)} ")

    pass
def act_25():
    fruits = ["apples", "banana", "orange"]

    fruits.append("strawberry")

    fruits.insert(1, "guyabano")

    fruitInsert = input("What fruit would you like to add?> ")

    fruits.append(fruitInsert)

    print(fruits)
def cc_1():
    print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b* * *\n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\t\t\b\b* * * * *\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b* * * * * * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b* * * * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b* * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t *")
def cc_2():
    name = input("please enter your name ---->")

    print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b* * *\n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\t\t\b\b\b* * * * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b *|" + name + "|*\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b* * * * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b* * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t *")
def cc_3():
    print("Dividing Numbers")
    num1 = eval(input("Enter the first number> "))
    num2 = eval(input("Enter the second number> "))


    answer = num1 / num2

    print(f"{num1} divided by {num2} = {answer}")
def cc_4():
    number1 = eval(input("Enter a number: "))

    number2 = eval(input("Enter a number: "))

    answer1 = number1 + number2

    answer2 = number1 - number2

    answer3 = number1 * number2

    answer4 = number1 / number2

    print("The sum of " , number1 , " and " , number2 , " is " , answer1)

    print("The difference of " , number1 , " and " , number2 , " is " , answer2)

    print("The product of " , number1 , " and " , number2 , " is " , answer3)

    print("The quotient of " , number1 , " and " , number2 , " is " , answer4)

def cc_5():
    print("\nWelcome to the Bank of Capistrano")

    name = input("\nPlease enter your name > ")

    print("\nHello," , name , "\b!\n")

    pera = eval(input("How much would you like to deposit? "))

    libo = pera // 1000
    libo2 = pera % 1000
    fiveh = libo2 // 500
    fiveh2 = libo2 % 500
    twoh = fiveh2 // 200
    twoh2 = fiveh2 % 200
    oneh = twoh2 // 100
    oneh2 = twoh2 % 100
    fifty = oneh2 // 50
    fifty2 = oneh2 % 50
    twenty = fifty2 // 20
    twenty2 = fifty2 % 20
    ten = twenty2 // 10
    ten2 = twenty2 % 10
    five = ten2 // 5
    five2 = ten2 % 5
    one = five2 // 1

    print("\n\t\t\tThe breakdown of your deposit is:")
    print("\t\t\t _______________________________")
    print("\t\t\t|\tValue\t |\tAmount\t|")
    print("\t\t\t|________________|______________|")
    print("\t\t\t|\t\t |\t\t|")
    print("\t\t\t|\t" , libo ,"\t | \t1,000\t|")
    print("\t\t\t|\t" , fiveh ,"\t | \t500\t|")
    print("\t\t\t|\t" , twoh ,"\t | \t200\t|")
    print("\t\t\t|\t" , oneh ,"\t | \t100\t|")
    print("\t\t\t|\t" , fifty ,"\t | \t50\t|")
    print("\t\t\t|\t" , twenty ,"\t | \t20\t|")
    print("\t\t\t|\t" , ten ,"\t | \t10\t|")
    print("\t\t\t|\t" , five ,"\t |\t5\t|")
    print("\t\t\t|\t" , one ,"\t |\t1\t|")
    print("\t\t\t|________________|______________|")

def cc_6():
        name = input("Enter your name: ")
        prelim = eval(input("Enter your Prelim grade: "))
        midterm = eval(input("Enter your Midterm grade: "))
        semifinal = eval(input("Enter your Semifinals grade: "))
        quiz = eval(input("Enter your quiz grade: "))
        finals = eval(input("Enter your Finals grade: "))
        project = eval(input("Enter your project grade: "))

        FG = (prelim * .15) + (midterm * .15) + (semifinal * .15) + (finals * .15) + (quiz * .15) + (project * .25)

        if FG > 100:
            print(f"Result:" , FG)
            print(f"your grade is too high {name}!")
        elif FG >= 75:
            print(f"Result:" , FG)
            print("congrats you passed")
        else:
            print("Result:" , FG)
            print("You failed, study more.")
def cc_7():
    A = input("DID YOU BUY A MEAT GOOD/s (yes/no)? ")
    if A.upper() == "YES":
        print('\nTHIS ARE THE LIST OF AVAILABLE MEAT GOODS')
        print('===========================================')
        print('Pork ------- 300php/kilo')
        print('Chicken ---- 250php/kilo')
        print('Beef ------- 400php/kilo')
        print('Rabbit ----- 250php/kilo')
        print('Tocino ----- 100php/kilo')
        print('Bacon ------ 120php/kilo')
        print('Bologna -----100php/kilo')
        quan1= eval(input("\nHow many kilos of Pork meat you want to buy? "))
        pork=quan1 * 300

        quan2= eval(input("\nHow many kilos of Chicken meat you want to buy? "))
        chicken=quan2 * 250

        quan3= eval(input("\nHow many kilos of Beef meat you want to buy? "))
        beef=quan3 * 400

        quan4= eval(input("\nHow many kilos of Rabbit meat you want to buy? "))
        rabbit=quan4 * 250

        quan5= eval(input("\nHow many kilos of Tocino meat you want to buy? "))
        tocino=quan5 * 100

        quan6= eval(input("\nHow many kilos of Bacon meat you want to buy? "))
        bacon=quan6 * 120

        quan7= eval(input("\nHow many kilos of Bologna meat you want to buy? "))
        bologna=quan7 * 100

        total= pork+chicken+beef+rabbit+tocino+bacon+bologna
        tax=(pork*0.123) or (chicken*0.123) or (beef*0.123) or (rabbit*0.123) or (tocino*0.123) or (bacon*0.123) or (bologna*0.123)
        total_and_tax= (total + tax)
        print()
        age = input("Are you a Senior Citizen(yes/no)? ")
        if age.lower() =='yes':
            disc=round(total*0.052)
            print(f"Hi, customer, you purhased a \n{quan1}kilo of Pork meat\n{quan2}kilo of Chicken meat\n{quan3}kilo of Beef meat\n{quan4}kilo of Rabbit meat\n{quan5}kilo of Tocino meat\n{quan6}kilo of Bacon meat\n{quan7}kilo of Bologna meat\nwith the total price of {total}php plus a 12.3% tax ({tax}php) and with a discount of 5.2% ({disc}php)")
        
        else:
            disc=0
            print(f"Hi, customer, you purhased a \n{quan1}kilo of Pork meat\n{quan2}kilo of Chicken meat\n{quan3}kilo of Beef meat\n{quan4}kilo of Rabbit meat\n{quan5}kilo of Tocino meat\n{quan6}kilo of Bacon meat\n{quan7}kilo of Bologna meat with the total price of {total}php plus a 12.3% tax(",tax,")")
        print()
        E = float(input("Amount Given: "))
        print()
        if E>= total_and_tax:
            change = round(E - total_and_tax + disc)
            print('=================RECEIPT===================')
            print('Qty.    Description           Amount')
            print(f'{quan1}x ----- PORK MEAT.........{pork}php')
            print(f'{quan2}x ----- CHICKEN MEAT......{chicken}php')
            print(f'{quan3}x ----- BEEF MEAT.........{beef}php ')
            print(f'{quan4}x ----- RABBIT MEAT.......{rabbit}php')
            print(f'{quan5}x ----- TOCINO MEAT.......{tocino}php')
            print(f'{quan6}x ----- BACON MEAT........{bacon}php')
            print(f'{quan7}x ----- BOLOGNA MEAT......{bologna}php')
            print()
            print(f'SUBTOTAL...................{total}php')
            print(f'TAX(12.3%).................{tax}php')
            print(f'TOTAL......................{total_and_tax}php')
            print(f'PAY AMOUNT.................{E}php')
            print(f'DISCOUNT(5.2%).............{disc}php') 
            print(f'CHANGE.....................{change}php')
            print()
            print("==THANK YOU COME AGAIN!!==")
        else:
            E< total_and_tax
            print("Insufficient Amount")
    else :
        print("Thankyou for stopping by!")
def cc_8():
    even = 0
    odd = 0
    sum = 0
    for x in range(1, 11):
        num = int(input(f"Enter {x} : "))
        sum += num 
        if num % 2 ==0 :
            odd += num 
        else :  
    
            even += num

    print(f"the sum of all number given is {sum}")
    print (f" the given number is {odd}")
    print(f"the given number is {even}")
def cc_9():
    for x in range(1,11) :
        for y in range(1, x + 1):
            print (" ", end = " ")
        for z in range (11, x, -1):
            print("*",end=" ")
        print()
def cc_10():
    for x in range(11,0,-1) :
        for y in range(1, x + 1):
            print (" ", end = " ")
        for z in range (11, x, -1):
            print("*",end=" ")
        for d in range (11, x, -1):
            print("*",end=" ")
        print()


    for x in range(1,11) :
        for y in range(1, x + 1):
            print (" ", end = " ")
        for z in range (11, x, -1):
            print("*",end=" ")
        for d in range (11, x, -1):
            print("*",end=" ")
        print()


def cc_11():
    for x in range(6,0, -1) :
        for y in range(1, x + 1):
            print (" ", end = " ")
        for z in range (7, x, -1):
            print("*",end=" ")
        for d in range (6, x, -1):
            print("*",end=" ")
        print()


    for x in range(0,7) : 
        for y in range(1, x +1):
            print (" ", end = " ")
        for z in range (7, x, -1):
            print("*",end= " ")
        for d in range (6, x, -1):
            print("*",end =" ")
        print()
def cc_12():
    for x in range (1,5):
        for y in range (5,x,-1):
            print( " ", end = " ")
        for z  in range (1, x + 1):
            print("*", end = " ")
        for w in range (1, x + 1):
            print("*", end = " ")
        print()

    for x in range (0,4):
        for y in range (4,0,-1):
            print( " ", end = " ")
        for z  in range (2,4):
            print("*", end = " ")
        for w in range (4,0,-1):
            print(" ", end = " ")
        print()
def cc_13():
    for x in range(1,7):
        for y in range(6,x,-1):
            print(" ", end = " ")
        for z in range (x, 1, -1):
            print(y, end = " ")
        for a in range (1,x + 1):
            print(a, end = " ")
        print()

    for x in range(5,0,-1):
        for y in range(6,x,-1):
            print(" ", end = " ")
        for z in range (x,1,-1):
            print(y, end = " ")
        for a in range (1,x + 1):
            print(a, end = " ")
        print()
def cc_14():
    tuloy = True
    a = 0
    while tuloy == True:
        number = eval(input("Enter a number--->  "))
        if number == 0:
            print("Program Terminated")
            print(f"The total of the number you enter is {a}")
            break

        else:
            a += number
            continue
def cc_15():
    import os

    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        elif ask.lower() == "yes":
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
        else:
            print("INVALID ANSWER it's only (yes/no)")
            continue
def cc_16():
    def denomination(amount):
        print("\nDenomination Breakdown:")
        a = amount // 1000
        b = amount % 1000

        c = b // 500
        d = b % 500

        e = d // 200
        f = d % 200

        g = f // 100
        h = f % 100

        i = h // 50
        j = h % 50

        k = j // 20
        l = j % 20

        m = l // 10
        n = l % 10

        o = n // 5
        p = n % 5

        q = p // 1

        print("1000---", a)
        print("500----", c)
        print("200----", e)
        print("100----", g)
        print("50-----", i)
        print("20-----", k)
        print("10-----", m)
        print("5------", o)
        print("1------", q)


    accounts = {}

    def create_account():
        u = input("Enter a username: ")
        if u in accounts:
            print("Account already exists!")
        else:
            accounts[u] = 0
            print(f"Account created successfully for {u}.")


    def deposit():
        u = input("Enter your username: ")
        if u in accounts:
            try:
                amt = int(input("Enter amount to deposit: "))
                if amt > 0:
                    accounts[u] += amt
                    print(f"Deposited {amt} successfully. New balance: {accounts[u]}")
                    denomination(amt)
                else:
                    print("Amount must be positive!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


    def withdrawal():
        u = input("Enter your username: ")
        if u in accounts:
            try:
                amt = int(input("Enter amount to withdraw (whole numbers only): "))
                if 0 < amt <= accounts[u]:
                    accounts[u] -= amt
                    print(f"Withdrawn {amt} successfully. Remaining balance: {accounts[u]}")
                    denomination(amt)
                else:
                    print("Insufficient funds or invalid amount!")
            except ValueError:
                print("Invalid input! Please enter a whole number.")
        else:
            print("Account not found!")


    def check_balance():
        u = input("Enter your username: ")
        if u in accounts:
            print(f"Your balance: {accounts[u]}")
        else:
            print("Account not found!")


    def options():
        while True:
            print("\nBanking System")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Choose an option (1-5): ")

            if choice == '1':
                create_account()
            elif choice == '2':
                deposit()
            elif choice == '3':
                withdrawal()
            elif choice == '4':
                check_balance()
            elif choice == '5':
                print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid option. Please try again.")

    options()
