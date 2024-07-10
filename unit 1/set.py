# Define some sets
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4}
s3 = {1, 2}
s4 = {1, 2, 3}

# Subset and Superset Examples
print(s1 <= s2)  # Output: True (s1 is a subset of s2)
print(s3 <= s1)  # Output: True (s3 is a subset of s1)

print(s1 < s2)   # Output: True (s1 is a proper subset of s2)
print(s1 < s4)   # Output: False (s1 is not a proper subset of s4, as they are equal)

print(s2 >= s1)  # Output: True (s2 is a superset of s1)
print(s1 >= s4)  # Output: True (s1 is a superset of s4)

print(s2 > s1)   # Output: True (s2 is a proper superset of s1)
print(s1 > s4)   # Output: False (s1 is not a proper superset of s4, as they are equal)
