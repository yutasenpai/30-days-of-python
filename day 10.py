# for i in range(13450):
#     print(i)
# count = 0
# while count < 3:
#     print(count)
#     # count += 1 

# ==========================================
# BLOCK 1: The Step-Down Counter
# ==========================================
print("="*50)
print("BLOCK 1: Counting Down")
print("="*50)

count = 10

while count >= 0:
    print(count, end=" ")
    count -= 1

# ==========================================
# BLOCK 2: The Multiples of 5 AP Series
# ==========================================
print("\n" + "="*50)
print("BLOCK 2: Multiples of 5")
print("="*50)

for i in range(1, 11):
    term = i * 5
    print(f"Term {i} is: {term}")

# ==========================================
# BLOCK 3: The Series Accumulator
# ==========================================
print("\n" + "="*50)
print("BLOCK 3: Series Accumulator")
print("="*50)

total_sum = 0
for i in range(1, 51):
    total_sum += i
    
print(f"The final grand total is: {total_sum}")
print("="*50)