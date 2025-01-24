# Let's create a virtual bartender that serves you if you are of legal age
drinks = ["Whiskey", "Rum","Tequila","Gin","Sake","Wine","Beer","Vodka","Champagne"]
mixers = ["Fanta","Fanta Limon","Red Bull","Tonic Water","Cola","Soda"]

import random

print("I am the virtual bartender, welcome to my bar")
name = input("What should I call you?")

try:
    age = input ("How old are you?")
    age = int(age)
    legal = None
    country = input("Where are you from?")
    if age < 14:
        legal = False
    elif age < 16:
        if country == "Austria":
            legal = True
        else:
            legal = False
    elif age < 18:
        if country == "Austria" or country == "Luxembourg":
            legal = True
        else:
            legal = False
    elif age < 21:
        if country == "USA" or country == "UAE":
            legal = False
        else:
            legal = True
    if legal:
        print(f"Here is a {choice(drinks)} {choice(mixers)}")
    else:
        print(f"I can only serve you {choice(mixers)}")
except ValueError:
    print("I don't have time for your games! Get out!")
