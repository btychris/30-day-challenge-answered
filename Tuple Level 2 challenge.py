fruits = ("Apple", "Orange", "Pineapple", "Blueberry")
vegetable = ("Cabbage", "Carrot")
animal_products = ("Milk", "Eggs", "Honey")

food_stuff_tp = fruits + vegetable + animal_products
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# middle_index = len(food_stuff_lt) // 2
# first_half = food_stuff_lt[:middle_index]
# second_half = food_stuff_lt[middle_index+1:]  # skips the cabbage
#
# print(first_half + second_half)

slicing = food_stuff_lt[3:-3]
print(food_stuff_lt)

food_stuff_tp = tuple(food_stuff_lt)

del food_stuff_tp