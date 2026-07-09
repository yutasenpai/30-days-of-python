def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'

dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}

# ⚡ This is where the magic happens:
print(unpacking_person_info(**dct))

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}, and your age is {age}.')
# except TypeError:
#     print('Type error occured')
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('Zero division error occured')

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except Exception as e:
#     print(e)

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
# numbers = [1, 2, 3, 4, 5, 6, 7]
# one, *middle, last = numbers
# print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*countries , es , ru = names

print("Countries:", countries)
print("ES:", es)
print("RU:", ru)

# big_list = list(range(1, 51))

# A list of the exact index locations you want to fetch
target_indices = [2, 2, 3, 1] 

# Loop through our targets and extract them from big_list
extracted_items = [names[i] for i in target_indices]

print(extracted_items)  # Outputs: [11, 23, 24, 29]

# 1. Grab 'Norway' using its index (2)
# norway = names[2]

# 2. Multiply a single-item list by 50
# norway_50_times = [norway] * int(input("Enter the number of times to print: "))

# print(norway_50_times)
# print(len(norway_50_times))  # Outputs: 50

from colorama import Fore, Style, init

# Initialize colorama (required to make it work perfectly on Windows)
init(autoreset=True)

valid_numbers = [10, 20, 30, 40, 50]

print("Available number: ", valid_numbers)

try:
    while True:
        try:
            # 1. Get the raw text first (this will NEVER crash)
            raw_input = input("Enter valid input from above list: ")
            
            # 2. Try to convert it to a number
            user_input = int(raw_input)
            
            # 3. Check the list
            if user_input in valid_numbers:
                print(f"Success! That number {user_input} is in list.")
                break
            else:
                print(f"{user_input} is not from the list. Enter valid number from given list above.")
    
        except ValueError:
            # 🎯 4. Now you can safely use raw_input here because it exists!
            print(f"Invalid input! '{raw_input}' is not a valid integer.")

except KeyboardInterrupt:
    print("\nProgram closed by user. Goodbye!")
