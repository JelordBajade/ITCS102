


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
