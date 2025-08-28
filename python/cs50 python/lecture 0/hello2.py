#   custom functions

def main():
    name = input("What's your name? ").title()
    hello(name)

def hello(to="world"): #    world is the default value when you don't add parameters in the function
    #   def - define can be used to create your own function
    #   to - parameter to a variable
    print("Hello,", to)

main()
#   name is in place of "to"
#   make sure to call the functions so it works