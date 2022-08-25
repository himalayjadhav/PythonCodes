# Faulty Calculator
print("Type + for addition")
print("Type - for subtraction")
print("Type * for multiplication ")
print("Type / for division")

type_of_cal = input()

p = "+"
q = "-"
r = "*"
s = "/"

A = int(input("Enter the first number :"))
B = int(input("Enter the second number :"))

if type_of_cal == p:  # For Addition
    if (A == 56) and (B == 9):
        print("Your answer is : 77")
    else:
        print("Your answer is : ", A + B)
elif type_of_cal == q:  # For subtraction
    print("Your answer is : ", A - B)
elif type_of_cal == r:  # For multiplication
    if (A == 45) and (B == 3):
        print("Your answer is : 555")
    else:
        print("Your answer is : ", A * B)
elif type_of_cal == s:  # For division
    if (A == 56) and (B == 6):
        print("Your answer is : 4")
    else:
        print("Your answer is : ", A / B)

print("Hope you had fun calculating :D")
