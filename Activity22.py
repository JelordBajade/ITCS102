#name listing and then count names

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