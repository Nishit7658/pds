# Simulate rolling a six-sided die 1000 times using the random module. Plot the # type: ignore
# frequency distribution of the outcomes (using basic text output or a simple
# bar chart).

import random

frequency = [0, 0, 0, 0, 0, 0]

for i in range(1000):
	roll = random.randint(1, 6)
	frequency[roll - 1] += 1

for i in range(6):
	print(i + 1, "::", frequency[i], "*" * (frequency[i] // 10))