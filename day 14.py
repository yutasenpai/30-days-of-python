from functools import reduce

# ==========================================
# EXERCISE 1 & 2: Theory Explanations
# ==========================================

print("=" * 70)

print("💡[EXERCISE 1] Core diffrence between Map, Filter and Reduce:")
print("   -map()    : A built in fuction that take a Function and Fterable.")
print("   -filter() : Filters the item which specify the filtering criteria.")
print("   -reduce() : Do not return Iterable, instead return single value.\n")

print("💡[EXERCISE 2] Functions vs Closures vs Decortator:")
print("   -Higher Order Functions : A Function that takes or returns another function.")
print("   -Closures : An inner function that remembers variables from its outer scope.")
print("   - Decorator: A wrapper used to add features to an existing function cleanly.")
print("=" * 70 + "\n")

# ==========================================
# IRL EXERCISE 1: E-COMMERCE CART DISCOUNTS (map)
# Scenario: A customer has items in their cart. Apply a 10% discount 
# to every single item price before showing them the checkout page.
# ==========================================

print("=" * 70)

cart_prices = [1000, 2500, 400, 800, 5000]

def price(x):
   return x * 0.9

discounted_prices = map(price, cart_prices)
# discounted_prices = list(map(lambda price: price * 0.9, cart_prices))

print("🛒 [IRL EXERCISE 1] E-COMMERCE DISCOUNT ENGINE:")
print(f"   Original Prices : {cart_prices}")
print(f"   Discounted (10%): {list(discounted_prices)}")
print("=" * 70 + "\n")

# ==========================================
# IRL EXERCISE 2: STREAMING APP USER CHECK (filter)
# Scenario: A premium content channel requires users to be at least 
# 18 years old. Filter out users who don't meet the restriction.
# ==========================================

print("="*70)

user_ages = [14, 22, 17, 35, 16, 28, 19]

# verified_viewers = list(map(lambda age: age>= 18, user_ages))
def verified_users (age):
   if age >= 18:
     return True
   return False

verified_viewers = list(filter(verified_users, user_ages))

print("📺 [IRL EXERCISE 2] AGE VERIFICATION FILTER:")
print(f"   All Sign-ups    : {user_ages}")
print(f"   Allowed Viewers : {verified_viewers}")
print("=" * 70 + "\n")

# ==========================================
# IRL EXERCISE 3: ANALYTICS REVENUE TRACKER (reduce)
# Scenario: An online shop wants to calculate the exact total revenue 
# generated from a sales campaign.
# ==========================================

print("=" * 70)
sales_transactions = [450, 1200, 300, 2150, 900]

# total_revenue = reduce(lambda total, sale: total + sale, sales_transactions)
def revenue(x, y):
    return int(x) + int(y)

total_revenue = reduce(revenue, sales_transactions)

print("💰[IRL EXERCISE 3] BUSINESS REVENUE ACCUMULATOR:")
print(f"   Sales Stream : {sales_transactions}")
print(f"   Total Revenue: ₹{total_revenue}")
print("=" * 70 + "\n")

# ==========================================
# IRL EXERCISE 4: DATA CLEANING MACHINE (Chaining Iterators)
# Scenario: Raw username registration logs contain accidental spaces 
# and mixed casing. Clean them by stripping spaces, turning them 
# uppercase, and filtering out invalid empty or short usernames.
# ==========================================

print("="*70)
raw_usernames = ["  rajver_s ", " sam", "   ", "alex_99  ", "bo"]

def change_upper(user):
   return user.upper()

def strip_space(user):
    return user.strip()

# cleanned_user = map(lambda name: name.upper().strip(), raw_usernames)
# final_database_names = list(filter(lambda name: len(name) > 3, cleanned_user))

cleanned_user = list(map(strip_space, raw_usernames))
upper_user = list(map(change_upper, cleanned_user))

def user_remove(name):
   if len(name) > 3:
     return name

final_database_names = list(filter(user_remove, upper_user))

print("⚙️ [IRL EXERCISE 4] DATABASE LOG CLEANER:")
print(f"   Raw Input log: {raw_usernames}")
print(f"   Cleaned Users: {final_database_names}")
print("=" * 70 + "\n")