from collections import Counter
from math import factorial

word = "ALGEBRA"
letter_counts = Counter(word)

distinct_permutations = factorial(len(word))
for count in letter_counts.values():
    distinct_permutations //= factorial(count)

print(distinct_permutations)