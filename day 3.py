# #==========================================
# #BLOCK 1: STUDY HOURS CALCULATOR
# #==========================================

#  hours = float(input("Enter the amount of hours you study per day:"))
#  weeks_in_year = 52
#  toal_hours = hours * weeks_in_year
#  print("You will study for", toal_hours, "hours in a year.")

#  if hours < 2:
#   print("You need to study more.")
#  elif hours == 2:
#   print("You are doing great.")
#  else:
#   print("You are a rockstar.")

# # ==========================================
# # BLOCK 2: TRIANGLE CALCULATOR
# #==========================================

#  base = float(input("Enter base of triangle: "))
#  height = float(input("Enter height of triangle:"))

#  area_of_triangle = 0.5 * base * height

#  print ("The area of the triangle is", area_of_triangle)

#  print ("-" * 30)

#  side_a = float(input("Enter side a:"))
#  side_b = float(input("Enter side b:"))
#  side_c = float(input("Enter side c:"))

#  perimeter_of_triangle = side_a + side_b + side_c
#  print ("The perimeter of the triangle is", perimeter_of_triangle)

#  print ("-" * 30)

#  if side_a == side_b == side_c:
#     print("The triangle is equilateral.")
    
# elif side_a == side_b or side_b == side_c or side_a == side_c:
# print ("The triangle is isosceles.")

# else:
#    print ("The triangle is scalene.")

# #==========================================
# #BLOCK 3:  QUADRATRIAL DETECTOR
# #==========================================

# print ("-" * 30)  
# print ("===QUADRATRIAL DETECTOR===")

# print ("-" * 30)

#  x1 = float(input("Enter x1:"))
#  y1 = float(input("Enter y1:"))
#  x2 = float(input("Enter x2:"))
#  y2 = float(input("Enter y2:"))      
#  x3 = float(input("Enter x3:"))
#  y3 = float(input("Enter y3:"))
#  x4 = float(input("Enter x4:"))
#  y4 = float(input("Enter y4:"))

#  print ("-" * 30)

# side_AB = ((x2 - x1) ** 2 + (y2 -y1) **2) **0.5
# side_BC = ((x3 - x2) ** 2 + (y3 -y2) **2) **0.5
# side_CD = ((x4 - x3) ** 2 + (y4 -y3) **2) **0.5
# side_DA = ((x1 - x4) ** 2 + (y1 -y4) **2) **0.5

# side_AC = ((x3 - x1) ** 2 + (y3 -y1) **2) **0.5
# side_BD = ((x4 - x2) ** 2 + (y4 -y2) **2) **0.5

# print("Calculated Dimensions:")
# print("  Sides    -> AB:", round(side_AB, 2), "| BC:", round(side_BC, 2), "| CD:", round(side_CD, 2), "| DA:", round(side_DA, 2))
# print("  Diagonals -> AC:", round(side_AC, 2), "| BD:", round(side_BD, 2))

# print ("-" * 30)

#  if side_AB == side_BC == side_CD == side_DA:
#      if side_AC == side_BD:
#          print("The quadrilateral is a square.")
#          print("Reason: All 4 sides are equal AND both diagonals are equal.")
#      else: 
#         print("The quadrilateral is a rhombus.")
#          print("Reason: All 4 sides are equal AND both diagonals are NOT equal.")
    
#  elif side_AB == side_CD and side_BC == side_DA:
#      if side_AC == side_BD:
#         print("The quadrilateral is a rectangle.")
#         print("Reason: Opposite sides are equal AND both diagonals are equal.")
#      else: 
#          print("The quadrilateral is a parallelogram.")
#          print("Reason: Opposite sides are equal AND both diagonals are NOT equal.")
        
#  else:
#      print("The quadrilateral is a general quadrilateral.")
#      print("Reason: It doesn't match a square, rectangle, rhombus, or parallelogram.")

#  print ("-" * 30)

# #==========================================
# # BLOCK 4: HEIGHTS & DISTANCES CALCULATOR
# #==========================================

# import math

# print ("-" * 40)
# print ("===HEIGHTS AND DISTANCE CALCULATOR===")
# print ("-" * 40)

# distance = float(input("Enter the distance from the observer to the object (In meters): "))
# angle_degrees = float(input("Enter the angle of elevation from the observer to the top of the object (In degrees): "))

# angle_radians = math.radians(angle_degrees)

# height = math.tan(angle_radians) * distance
# print ("-" * 40)
# print("The height of the object is approximately:", round(height, 2), "meters.")
# print ("-" * 40)

import random

print ("-" * 40)
print ("===🎯RANDOM NUMBER GUESSING GAME🎯===")
print ("-" * 40)
print("I'm thinking of a number between 1 and 100, Can you guess it?🤔 You have 8 attempts. Good luck! 🍀")

secret_number = random.randint(1, 100)
attempts_left = 8
score = 100

while attempts_left > 0:
    print("-" * 40)
    print(f"Lives Left: {attempts_left} | Current Score: {score}")
    guess = int(input("Enter your guess (between 1 and 100): "))
    
   
    if guess == secret_number:
        print("\nBOOM!🎊 Your guess is correct!")
        print(f"Indeed, the secret number was {secret_number}.")
        print(f"Your final score is: {score} points.")
        break  # Python now sees this perfectly inside the while loop!
        
    elif guess < secret_number:
        print("Too low! Try a bigger number.⬆️")
        score = score - 12.5
        attempts_left = attempts_left - 1
        
    else:
        print("Too high! Try a smaller number.⬇️")
        score = score - 12.5
        attempts_left = attempts_left - 1


if attempts_left == 0:
    print("\n💀 GAME OVER, BRO!")
    print(f"You ran out of lives. The secret number was actually {secret_number}.")
    print("Better luck next time!")

print("=" * 40)