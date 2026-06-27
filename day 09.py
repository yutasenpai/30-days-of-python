# # ==========================================
# # BLOCK 1: LEVEL 1
# # ==========================================

# 1. DRIVING AGE CHECKER

# print("="*70)
# user_age = int(input("Enter your age: "))

# if user_age >= 18:
#     print("Your are eligible to learn driving.✅")
# else:
#     missing_years = 18 - user_age
#     print(f"You have to wait {missing_years} years before driving.😓")

# print("="*70)

# # 2. AGE COMPARETOR 

# my_age = 15
# if user_age > my_age:
#     diff = user_age - my_age
#     year_word = "year" if diff ==1 else "years"
#     print(f"You are {diff} {year_word} older than me.😓")
# elif user_age < my_age:
#      diff = my_age - user_age
#      year_word = "year" if diff == 1 else "years"
#      print(f"I am {diff} {year_word}older than you.😂")
# else:
#      print("Wow! You and me are same age.🤯")

# print ("="*70)

# # 3. Number Comparator
# print("Number Comparator")
# print("="*70)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print("="*70)

# if a > b:
#     print(f"{a} is bigger than {b}.")
# elif a < b:
#     print(f"{b} is bigeer than {a}.")
# else:
#     print(f"{a} and {b} are equal.")

# print("="*70)
# # ==========================================
# # BLOCK 2: The AP Term Checker Logic Engine
# # ==========================================

# print("="*70)
# print("The AP Term Checker Logic Engine")
# print("="*70)

# a = int(input("Enter first term (a): "))
# d = int(input("Enter the diffrence (d): "))
# n = int(input("Enter the term number (n) you want to calculate:"))
# print("="*70)

# if n <= 0:
#     print("🚨 Error: Term number must be greater than 0!")
# else:
#      an = a + (n-1)*d

# if 11<= n % 100 <= 13:
#      suffix = "th"
# else:
#      last_digit = n % 10
# if last_digit==1:
#      suffix = "st"
# elif last_digit==2:
#      suffix = "nd"
# elif last_digit==3:
#      suffix = "rd"
# else:
#      suffix = "th"

# print(f"The {n}{suffix} term is {an}.")
# print("="*70)

