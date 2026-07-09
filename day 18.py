# import re
# from collections import Counter
# txt = 'I love to teach python and javaScript'
# # It returns an object with span, and match
# match = re.match('I love to teach', txt, re.I)
# print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# # We can get the starting and ending position of the match as tuple using span
# span = match.span()
# print(span)     # (0, 15)
# # Lets find the start and stop position from the span
# start, end = span
# print(start, end)  # 0 15
# substring = txt[start:end]
# print(substring)       # I love to teach

# paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
# words = re.findall(r'\w+', paragraph.lower())
# words_count = Counter(words)

# sorted_word_counts = words_count.most_common()
# print(sorted_word_counts)

import re
# ==========================================
# BLOCK 1: Total Cost
# ==========================================

product_data = "Item1 costs 4500 INR, Item2 costs 1200 INR, and the premium subscription is 750 INR."

pattern = r'(\d+)\sINR'
prices_as_strings = re.findall(pattern, product_data)

print("Extracted Prices:", prices_as_strings)

prices_as_ints = [int(price) for price in prices_as_strings]

total_cost = sum(prices_as_ints)

print("Total Cost: ", total_cost)

# ==========================================
# BLOCK 2: Username
# ==========================================

usernames_to_test = ['rachna_kaur', 'rajveer-teachings', 'player_123', 'hello@world']
while true:
    if usernames_to_test(-@):
        print(False)