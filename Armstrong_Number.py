for i in range(1001):
    copy_i = i
    sum = 0
    order = len(str(i))

    while i > 0:
        digit = i % 10
        sum = sum + digit **order
        i = i // 10
    if sum == copy_i:
        print(copy_i)
