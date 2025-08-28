#   x = input("What would x be? ")
#   y = input("What would y be? ")
#   you are able to nest functions, so instead of typing that out ...


#   use int for regular numbers
#   float for decimals
x = float(input("What would x be? "))
y = float(input("What would y be? "))

z = x / y # "ndigits" allows for the argument to have 2 decimal points
#   round(number[, ndigits])

print(f"{z:.2f}") # string approach, same as   z = round(x / y, 2)
#   adds comma to format string

#   square brackets are optional, specify # of digits if wanted


#   comes from the keyboard as strings, so it counts string length
#   we can do str to int like this:

#   z = int(x) + int(y)
#   function to convert numeric string to integers
#   print(z)