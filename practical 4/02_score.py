# Create two lists representing Math and Science scores. Calculate the
# Covariance and Correlation Coefficient between them using basic Python
# formulas or numpy.

math_score = list(map(float, input("Enter the Math scores separated by space :: ").split()))
science_score = list(map(float, input("Enter the Science scores separated by space :: ").split()))

if len(math_score) == len(science_score):
	math_mean = sum(math_score) / len(math_score)
	science_mean = sum(science_score) / len(science_score)

	covariance = 0
	math_variance = 0
	science_variance = 0

	for i in range(len(math_score)):
		math_difference = math_score[i] - math_mean
		science_difference = science_score[i] - science_mean

		covariance += math_difference * science_difference
		math_variance += math_difference ** 2
		science_variance += science_difference ** 2

	covariance = covariance / len(math_score)
	correlation = covariance / ((math_variance / len(math_score)) ** 0.5 * (science_variance / len(science_score)) ** 0.5)

	print("Covariance :: ", covariance)
	print("Correlation coefficient :: ", correlation)
else:
	print("Both lists must contain the same number of scores.")