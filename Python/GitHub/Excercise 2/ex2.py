user_input = str(input("Enter text: "))

upper_case_counter = 0

for i in user_input:
    if i.isupper():
        upper_case_counter += 1

print(f'The input text contains {upper_case_counter} uppercase characters.')