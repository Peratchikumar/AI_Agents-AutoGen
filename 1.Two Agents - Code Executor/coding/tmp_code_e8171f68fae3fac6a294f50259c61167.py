from math import factorial
from collections import Counter

word = "ALGEBRA"
counts = Counter(word)

result = factorial(len(word))
for count in counts.values():
    result //= factorial(count)

print(result)