# Calculate the probability of drawing an Ace from a standard deck of 52
# cards using a Python simulation.

import random

deck = ["Ace"] * 4 + ["Other"] * 48
total_draws = 1000
ace_count = 0

for i in range(total_draws):
	card = random.choice(deck)
	if card == "Ace":
		ace_count += 1

probability = ace_count / total_draws

print("Number of Aces drawn :: ", ace_count)
print("Total number of draws :: ", total_draws)
print("Probability of drawing an Ace :: ", probability)