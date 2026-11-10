import math
from collections import Counter

word = "ALGEBRA"
counts = Counter(word)

result = math.factorial(len(word))
for count in counts.values():
    result //= math.factorial(count)

print(result)