# Getting the chance of rain as a float
rain_chance = float(input("Enter chance of rain (from 0 to 1): "))

# Printing mood rating scale
print("\nVery nice    - 10")
print("Nice         -  8")
print("Satisfactory -  6")
print("Bad          -  3")
print("Very bad     -  1")
print("According to these key-values, you will rate your mood\n")

# Getting mood ratings as integers
home_rain = int(input("Rate your mood when you are at home and it's sunny: "))
home_sun = int(input("Rate your mood when you are at home and it's rainy: "))
forest_rain = int(input("Rate your mood when you are in the forest and it's rainy: "))
forest_sun = int(input("Rate your mood when you are in the forest and it's sunny: "))

# Calculating usefulness using the provided formula
w_home = rain_chance * home_rain + (1 - rain_chance) * home_sun
w_forest = rain_chance * forest_rain + (1 - rain_chance) * forest_sun

# Displaying the results
print(f"\nUsefulness of staying at home is {w_home}, and going to the forest is {w_forest}")
print("Result: ")
# Recommending based on usefulness
if w_home > w_forest:
    print("We recommend you to stay at home")
else:
    print("We recommend you to go to the forest")
