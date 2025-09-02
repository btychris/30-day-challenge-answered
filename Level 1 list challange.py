# # muscles = ["Chest", "Shoulder", "Triceps", "Biceps", "Abs"]
# # print(muscles)
# # print(f"There are {len(muscles)} in the list")
# # print(f"First item: {muscles[0]}")
# # print(f"Middle item: {muscles[2]}")
# # print(f"Last item: {muscles[4]}")
#
# # mixed_data_types = ["Chris", 18, 177, "No", "Somewhere"]
#
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(f"There are {len(it_companies)} in the list")
print(f"First item: {it_companies[0]}")
print(f"Middle item: {it_companies[2]}")
print(f"Last item: {it_companies[4]}")

# Modifying list
it_companies[0] = "Samsung"
print(it_companies)

# Adding to list
it_companies.append("Nvida")
print(it_companies)

# insert to list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, "Alphabet inc.")
print(it_companies)

it_companies[2] = "Microsoft"
print(it_companies)

joined_companies = "#; ".join(it_companies)
print(joined_companies)

print("Samsung" in it_companies)
print("Orange" in it_companies)

it_companies.sort()
print(it_companies) # Alphabetical order

it_companies.sort(reverse=True)
print(it_companies)
print("\n")
print(it_companies)
print(it_companies[3:])
print(it_companies[:-3])
print(it_companies[:3] + it_companies[5:])

it_companies.remove(it_companies[0])
print(it_companies)

it_companies.remove(it_companies[-1])
print(it_companies)

it_companies.remove(it_companies[middle_index])
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, "Python")
print(full_stack)

full_stack.insert(6, "SQL")
print(full_stack)