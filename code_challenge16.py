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