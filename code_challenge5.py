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