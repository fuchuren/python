def main():
    x = int(input("What would you like to put for x? "))
    #   int = converted version of user's input
    print("x squared is", square(x))
    print("x cubed is", cube(x))

def square(n): #    n represents a number
    return pow(n, 2)
#   return n * n,   return n ** 2,  return pow(n, 2)    for exponents
#   return the actual value

def cube(n):
    return pow(n, 3)

main()