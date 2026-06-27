# # 1. Defining the function
# def greet_user():
#     print("Welcome to Day 11 of Python!")

# # 2. Calling the function
# greet_user()  # Output: Welcome to Day 11 of Python!

# def greet_person(name):
#     print(f"Hello, {name}!")

# def square_number(x):
#     return x * x

# result = square_number(5)
# print(result)  # Output: 25

# ==========================================
# BLOCK 1: The Evens or Odds Checker
# ==========================================

# print("="*70)
# print("The Evens or Odds Checker")
# print("="*70)

# def The_Evens_Odds(num_to_check):
#     if number % 2 == 0:
#         print(f"{num_to_check} is even.")
#     else:
#         print(f"{num_to_check} is odd.")

# number = int(input("Enter the number: "))
# The_Evens_Odds(number)

# print("="*70)

# ==========================================
# BLOCK 2: The AP Sum Calculator
# ==========================================
print("="*70)
print("The AP Sum Calculator")
print("="*70)

def sum_of_ap(a, d, n):
    if n<= 0:
        return 0
    sn = (n / 2) * (2 * a + (n - 1) * d)
    return sn

first_term = int(input("Enter first term (a): "))
diff = int(input("Enter common difference (d): "))
terms = int(input("Enter total terms to sum up (n): "))

total = sum_of_ap(first_term, diff, terms)

print("="*70)
print(f"The sum of the first {terms} terms is: {total}")
print("="*70)