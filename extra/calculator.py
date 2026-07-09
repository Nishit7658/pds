people = int(input("Enter how many people you are :: "))
amount = int(input("How much your bill is :: "))
tip = int(input("How much percent of tip you want to give :: "))
tip = tip / 100

amount_to_pay_by_each_person = ((amount * tip) + amount) / people

print("Each person should pay :: " + str(amount_to_pay_by_each_person))
