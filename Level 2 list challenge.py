ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

print(min(ages))
print(max(ages))
print(ages)

median = len(ages) // 2
print(f"The median in the list is: {ages[median]}")

average = sum(ages) / len(ages)
print(f"The average ages is: {average}")

print(f"The range of the ages are: {max(ages) - min(ages)}")

print(abs(min(ages) - average))
print(abs(max(ages) - average))
