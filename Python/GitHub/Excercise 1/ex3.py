first_number = (int(input("1st number: ")))
second_number = (int(input("2nd number: ")))

addition = first_number + second_number
difference = abs(first_number - second_number)
product = first_number * second_number
power = first_number ** second_number
quotient_int = int(first_number / second_number)
quotient_float = float(first_number / second_number)
remainder = first_number % second_number

print(f"Sum: {addition}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Power: {power}")
print(f"Quotient (int): {quotient_int}")
print(f"Quotient (float): {quotient_float}")
print(f"Remainder: {remainder}")
