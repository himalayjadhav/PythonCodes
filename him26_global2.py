x = 55
def harry():
    x = 43
    def rohan():
        global x
        x = 24
    print("Before rohan() has been called", x)
    rohan()
    print("After rohan() has been called", x)
harry()
print(x)