# import math
# print(math.pi)

# users = {'name':'Asab', 'age':250, 'country':'Finland'}
# print(users['name'])
# print(users['country'])

# print(4 + float('3'))
# print(math.pow(2,3))
# print(1/1)


# ====================================================================
# 💻 CODE REPAIR SHOP: DAY 15 EXERCISES
# Fix the errors in each section so the entire script prints cleanly!
# ====================================================================

# 🔧 BUG 1: SyntaxError & NameError
print("=" * 70)
print("🔧 FIXING BUG 1...")
username = "Rajveer"
print(f"   User tracking initialized: {username}")
print("=" * 70)

# 🔧 BUG 2: IndexError
print("🔧 FIXING BUG 2...")
tools = ["Map", "Filter", "Reduce"]
print(f"   The third tool is: {tools[2]}")
print("=" * 70)

# 🔧 BUG 3: TypeError & ValueError
print("🔧 FIXING BUG 3...")
current_age = 24
years_to_add = 2
new_age = current_age + years_to_add
print(f"   Next birthday age: {new_age}")
print("=" * 70)

# 🔧 BUG 4: KeyError
print("🔧 FIXING BUG 4...")
profile = {"name": "Rachna", "city": "Delhi"}
print(f"   User is located in: {profile['city']}")
print("=" * 70)

# 🏆 VICTORY BANNER
print("\n🎉 CONGRATULATIONS! ALL BUGS ARE DEFEATED! 🎉\n")