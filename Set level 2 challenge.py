A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)
print(C)

print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))


new_A = A.union(B)
new_B = B.union(A)
print(new_A.union(new_B))

print(A.symmetric_difference(B))

del A
del B
del C
del new_A
del new_B
