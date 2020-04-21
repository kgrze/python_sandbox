
# Naive method
squares = []
for n in range(10):
    squares.append(n ** 2)
print(squares)

# Better, using map()
squares = list(map(lambda n: n**2, range(10)))
print(squares)

# Best, using list comprehension
squares = [n ** 2 for n in range(10)]
print(squares)

# Another example of selecting EVEM subset from list using filter and comprehension
# using map and filter
sq1 = list(
    map(lambda n: n ** 2, filter(lambda n: not n % 2, range(10)))
    )
# equivalent, but using list comprehensions
sq2 = [n ** 2 for n in range(10) if not n % 2]
print(sq1, sq1 == sq2)  # prints: [0, 4, 16, 36, 64] True

# Nested comprehensions
items = 'ABCD'
pairs = []
for a in range(len(items)):
    for b in range(a, len(items)):
        pairs.append((items[a], items[b]))
print(pairs)

# The same output using nested list comprehension
pairs = [(items[a], items[b]) for a in range(len(items)) for b in range(a, len(items))]
print(pairs)

# Filtering comprehension
from math import sqrt
# this will generate all possible pairs
mx = 10
triples = [(a, b, sqrt(a**2 + b**2))
    for a in range(1, mx) for b in range(a, mx)]

# this will filter out all non pythagorean triples
#triples = filter(lambda triple: triple[2].is_integer(), triples)
#triples = list(map(lambda triple: triple[:2] + (int(triple[2]), ), triples))
triples = [(a, b, int(c)) for a, b, c in triples if c.is_integer()]

print(triples)  # prints: [(3, 4, 5), (6, 8, 10)]

# Dict comprehension
from string import ascii_lowercase
lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
# lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)} 
print(lettermap)
