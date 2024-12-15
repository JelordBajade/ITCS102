name = input("Please enter your name: ")
deposit = eval(input("Please enter amount to deposit: "))

answer1 = deposit // 1000
num1 = deposit % 1000 

answer2 = num1 // 500
num2 = num1 % 500

answer3 = num2 // 200
num3 = num2 % 200

answer4 = num3 // 100
num4 = num3 % 100

answer5 = num4 // 50
num5 = num4 % 50

answer6 = num5 // 20
num6 = num5 % 20

answer7 = num6 // 10
num7 = num6 % 10

answer8 = num7 // 5
num8 = num7 % 5

answer9 = num8 // 1

print("Hi" , name , "the breakdown of your deposit is:")
print(answer1 , "- 1000")
print(answer2 , "- 500") 
print(answer3 , "- 200")
print(answer4 , "- 100")
print(answer5 , "- 50")
print(answer6 , "- 20")
print(answer7 , "- 10")
print(answer8 , "- 5")
print(answer9 , "- 1")
