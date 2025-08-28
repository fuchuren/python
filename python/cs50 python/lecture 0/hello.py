name = input("What's your name? ").strip().title()

#   the new variable is name, where the function is input
#   we can add the following methods after the variable

#   name = name.strip()
#   = is an assignment operator , "strip" removes whitespace from string
#   name = name.capitalize() - capitalizes name
#   name = name.title() # titlecases name instead

first, last = name.split(" ")

print(f"Hello,", {first} + ".", "Nice to meet you.")

#   this is a formatted string