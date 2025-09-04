it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(f"There are {len(it_companies)} it companies in the set")

it_companies.add("Twitter")
print(it_companies)

it_companies.update(["Twitter", "Samsung", "Accenture", "Nvida", "Alphabet inc"])
print(it_companies)

# Remove will raise an error if an item cannot be found, while discard will not