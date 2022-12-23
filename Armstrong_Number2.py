n = input("Enter a number:\n")
sum = 0
copy_n = n
order = len(str(n))

for i in n:
    sum = sum + int(i)**order
print("The addition is:",sum)

if sum == int(copy_n):
    print(copy_n,"is an Armstrong Number")
else:
    print(copy_n,"is not an armstrong Number")
