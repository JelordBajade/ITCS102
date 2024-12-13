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