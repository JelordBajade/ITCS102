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