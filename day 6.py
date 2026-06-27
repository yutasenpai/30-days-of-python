# # Step 1: Start with a locked tuple
# modes_of_transport = ("Car", "Metro", "Train")

# # Step 2: Convert to a list using the list() function
# transport_list = list(modes_of_transport)

# # Step 3: Modify the list freely
# transport_list.append("Airplane")

# # Step 4: Convert it back to a locked tuple using tuple()
# modes_of_transport = tuple(transport_list)

# transport_list.append("Plane")

# print(modes_of_transport)  # Output: ('Car', 'Metro', 'Train', 'Airplane')

# print("=" * 40)
# print("🎯 DAY 6: TUPLE ANALYTICS")
# print("=" * 40)

# # 1. Setting up your raw data groups
# fruits = ("Mango", "Banana", "Orange")
# vegetables = ("Potato", "Tomato", "Onion")
# animal_products = ("Milk", "Butter", "Cheese")

# # TODO: Step A
# # Join all three tuples into one giant master tuple called 'food_stuff_tp' using the + operator.

# food_stuff_tp = list(fruits + vegetables + animal_products) 
# food_stuff_tp = tuple(food_stuff_tp)     

# # TODO: Step B
# # Create a new list called 'food_stuff_lt' by converting your 'food_stuff_tp' tuple into a list.

# food_stuff_lt = list(food_stuff_tp)

# # TODO: Step C
# # Use your list methods to add "Chicken" to the end of 'food_stuff_lt', 
# # then convert it right back into the 'food_stuff_tp' tuple.

# food_stuff_lt.append ("Chicken")
# food_stuff_tp = tuple(food_stuff_lt)

# # TODO: Step D (Unpacking)
# # We have a tuple with 3 items:
# profile_data = ("Rajveer", 14, 5.4)
# # Unpack this tuple into three separate variables named: name, age, height
# # Then print them out using an f-string!

# name, age, height = profile_data
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"Height: {height}")

# # Final check prints
# print("Updated Food Tuple:", food_stuff_tp)
# print("-" * 40)