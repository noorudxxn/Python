import random
import math

names = input("Enter customer names separated by commas: ")

name_list = [name.strip() for name in names.split(",")]

unique_names = list(set(name_list))

random.shuffle(unique_names)

if len(unique_names) < 2:
    print("Please enter at least 2 unique names.")
else:
    winners = random.sample(unique_names, 2)

    winner1 = winners[0]
    winner2 = winners[1]

    print("Lucky Draw Winners:")
    print("Winner 1:", winner1[::-1])
    print("Winner 2:", winner2[::-1])

    total_participants = len(unique_names)

    print("Total unique participants:", total_participants)

    sqrt_value = round(math.sqrt(total_participants))

    print("Rounded square root:", sqrt_value)