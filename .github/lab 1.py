# Callie Walker and Lesdy Galvez
# Course: CS151, Dr. Rajeev
# Date: 9/16/21
# Lab Number: 1
# Program Inputs: Request the number of milliters and assign the conversions equations for teaspoons and tablespoons.
# Program Output: The program will output the conversion in tablespoon and teaspoons.

milliliters = input("Enter the amount of milliliters: ")
milliliters_int = int(milliliters)
convertTeaspoon = (milliliters_int / 5)
convertTablespoon = (convertTeaspoon / 3)

print("The teaspoons are ", convertTeaspoon , " and the tablespoons are " , convertTablespoon)
