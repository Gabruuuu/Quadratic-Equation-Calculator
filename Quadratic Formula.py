print("Quadratics calculator ")

print("Created by Gabriel Palomero")

print("Please enter A, B, and C from the standard quadratic equation")

first_number = int ( input ( " Enter 'A' : "))

second_number = int ( input ( " Enter 'B' : "))

third_number = int ( input ( " Enter 'C' : "))

import math

quadratic_formula = ((-1*second_number) + math.sqrt((second_number**2) - (4 * first_number *third_number))) / (2 * first_number)

quadratic_formula_2 = ((-1*second_number) - math.sqrt((second_number**2) - (4 * first_number *third_number))) / (2 * first_number)

print("x =", quadratic_formula, "  x =", quadratic_formula_2)
