# ==========================================
# BLOCK 1: RANDOM ID & COLOR GENERATION
# ==========================================

# print("="*70)
# print("RANDOM ID & COLOR GENERATION")
# print("="*70)

# import string
# import random

# # def random_user_id():
# #     charecters = string.ascii_lowercase + string.digits
# #     user_id = "".join(random.choices(charecters, k=6))
# #     return user_id

# # print(f"Random 6-char id: {random_user_id()}.")
# # print("-"*60)

# def random_user_id():

#     charecter_count = int(input("Enter the number of charcters for generation: "))
#     user_id = int(input("Enter the number of id needed to be generated: "))

#     pool = string.ascii_letters + string.digits
#     print(f"\nGenrating {user_id} with length {charecter_count}.")

#     for _ in range(user_id):
#         genrated_id = "".join(random.choices(pool, k=charecter_count))
#         print(genrated_id)

# random_user_id()

# print("-"*60)
# ==========================================
# BLOCK 2: The E-commerce Invoice Tracking Generator
# ==========================================

# print("="*70)
# print("The E-commerce Invoice Tracking Generator")
# print("="*70)

# import string
# import random

# def tracking_id(prefix):
#     pool = string.ascii_uppercase 
#     random_id = "".join(random.choices(pool, k=4))
#     completed_id = f"{prefix}-2026-{random_id}"
#     return completed_id

# invoice_id = tracking_id("BLJ")

# print(f"Your tracking id is {invoice_id}.")
# print("="*70)

# ==========================================
# BLOCK 3: The Campaign Giveaway Winner Picker
# ==========================================

# print("="*70)
# print("The Campaign Giveaway Winner Picker")
# print("="*70)

# import random

# def pick_winners(participant_list):
#     random_winners = random.sample(participant_list, k=3)
#     return random_winners

# entrants = ["Amit_99", "Riya.S", "Kabir_vlogs", "Simran_K", "TechGamer", "Vikas_Delhi"]
# lucky_draw = pick_winners(entrants)

# if lucky_draw:
#     print(f"🏆 Grand Prize Winner : {lucky_draw[0]}")
#     print(f"🥈 Runner-up 1       : {lucky_draw[1]}")
#     print(f"🥉 Runner-up 2       : {lucky_draw[2]}")

# print("="*70)

# ==========================================
# BLOCK 3: The Athlete Performance Consistency Tracker
# ==========================================

print("="*70)
print("The Athlete Performance Consistency Tracker")
print("="*70)

import statistics

weekly_train = []

for day in range(1, 8):
    mintues_trained = int(input(f"Enter the minutes trained for day {day}(in mintues):"))
    weekly_train.append(mintues_trained)

avg_time = statistics.mean(weekly_train)
consistency_score = statistics.stdev(weekly_train)

print("="*70)
print(f"🔥Avg time: {avg_time: .1f} mins")
print(f"🎯Consistency score: {consistency_score: .1f}")
print("="*70)