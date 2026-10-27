import random
import math

names = input("Enter guest names separated by commas: ")

name_list = [name.strip() for name in names.split(",")]

unique_names = list(set(name_list))

selected_name = random.choice(unique_names)

reversed_name = selected_name[::-1]

total_names = len(unique_names)

sqrt_value = round(math.sqrt(total_names))

print("Unique names:", unique_names)
print("Selected name:", selected_name)
print("Reversed name:", reversed_name)
print("Total unique names:", total_names)
print("Rounded square root:", sqrt_value)