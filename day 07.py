# # Starting data given by the exercise
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# # 1. Find the length of the set it_companies
# print("1. Total IT Companies:", len(it_companies))

# # 2. Add 'Twitter' to it_companies
# it_companies.add('Twitter')
# print("2. After adding Twitter:", it_companies)

# # 3. Insert multiple IT companies at once
# it_companies.update(['Meta', 'Netflix', 'TCS'])
# print("3. After adding multiple companies:", it_companies)

# # 4. Remove one of the companies (let's remove Oracle)
# it_companies.remove('Oracle')
# print("4. After removing Oracle:", it_companies)

# # 5. What is the difference between remove and discard?
# print("\n5. Difference explanation:")
# # .remove() will CRASH your code with a KeyError if the item isn't found.
# # .discard() will NOT crash your code; it just does nothing if the item isn't there.


# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}

# # 1. Join A and B (Union)
# print("1. Union of A and B:", A.union(B))

# # 2. Find A intersection B (Common elements)
# print("2. Intersection of A and B:", A.intersection(B))

# # 3. Is A subset of B? (Are all items of A inside B?)
# print("3. Is A a subset of B?:", A.issubset(B))

# # 4. Are A and B disjoint sets? (Do they have ZERO common items?)
# print("4. Are A and B disjoint?:", A.isdisjoint(B))

# # 5. Join A with B and B with A (Using the | pipe operator shortcut)
# print("5. A | B:", A | B)
# print("   B | A:", B | A)

# # 6. What is the symmetric difference between A and B? (Items NOT shared)
# print("6. Symmetric Difference:", A.symmetric_difference(B))

# # 7. Delete the sets completely from memory
# del A
# del B

# age = [22, 19, 24, 25, 26, 24, 25, 24]

# # 1. Convert the ages to a set and compare lengths
# age_set = set(age)
# print("1. List length:", len(age), "| Set length:", len(age_set))
# print("   Which is bigger? The List is bigger because the Set deleted all duplicate ages.")

# # 2. Difference between data types:
# """
# - String: Text characters locked in order. Immutable.
# - List: Ordered collection. Mutable (changeable). Allows duplicates.
# - Tuple: Ordered collection. Immutable (locked). Allows duplicates.
# - Set: Unordered collection. Mutable. Must be completely UNIQUE (no duplicates).
# """

# # 3. Count unique words in a sentence
# sentence = "I am a teacher and I love to inspire and teach people."

# # Clean the period out and split into a list of words
# words_list = sentence.replace('.', '').split()

# # Throw the list into a set to wipe out duplicates like "I" and "and"
# unique_words = set(words_list)

# print("\n3. Total words in sentence:", len(words_list))
# print("   Total UNIQUE words:", len(unique_words))
# print("   The unique words are:", unique_words)

#  ==========================================
#  BLOCK 1: The Class 10 Math Test
#  ==========================================
# print("=" * 70) 
# print("BLOCK 1: The Class 10 Math Test")
# print("="* 70)
# maths_submitted = {1, 3, 5, 7, 9, 11, 12, 15}
# science_submitted = {3, 4, 7, 8, 11, 14, 15, 19}

# print("The students who submitted both assigments:", maths_submitted.intersection(science_submitted))
# print("=" * 70)
# print("The students who submitted only the Maths assignment:", maths_submitted.difference(science_submitted))
# print("=" * 70)
# print("The list of all students who have submitted at least one assignment:", maths_submitted.symmetric_difference(science_submitted))
# print("=" * 70)

# ==========================================
# BLOCK 2: The Typo Cleaner
# ==========================================

# print("-" * 50)
# print("BLOCK 2: The Typo Cleaner")
# print("-"* 50)

# user_input = [10, 20, 20, 30, 40, 40, 50]
# clean_set = set(user_input)

# print("Cleaning duplicates:", clean_set)
# print("-" * 50)

# clean_set.update([60, 70])
# print("Updated set:", clean_set)

# print("-" * 50)
# print("Length of set:", len(clean_set))
# print("-" * 50)

# ==========================================
# BLOCK 3: The Username Security Guard
# ==========================================
# print("=" * 50)
# print("BLOCK 3: The Username Security Guard")
# print("=" * 50)

# taken_usernames = {"rajveer_10", "python_coder", "alpha_dev"}
# while True:
#     new_user = input("Enter your Username (or type 'exit' to quit):\n👉 ")
    
#     if new_user.lower() == 'exit':
#         print("Closing Security Guard System. Goodbye! 👋")
#         break  

#     if new_user in taken_usernames:
#         print("🚨 Username already exists!")
#     else: 
#         taken_usernames.add(new_user)
#         print("✅ Registration successful!")
#         print(f"Updated User Database: {taken_usernames}")