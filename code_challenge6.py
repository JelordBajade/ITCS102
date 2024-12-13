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