name = input("What is your name? ")
age2 = input(f"How old are you {name}? ")
try:
    age2 = int(age2)
    print(f"{name} based on my advanced calculations, you were born in {2024-age2}")
    7/0
except ValueError:
    print("Please enter a valid value for age")
    print("I can also print this in case of error that I prevented")
except ZeroDivisionError:
    print("You can't divide by zero")
except:
    print("This is another type of error")
else:
    print("Thanks for playing the game as expected")
finally:
    print("Thanks for playing the game")