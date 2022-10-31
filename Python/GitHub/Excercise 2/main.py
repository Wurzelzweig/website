start_input = int(input('Start: '))
stop_input = int(input('Stop: '))
step_input = int(input('Step: '))

odd_counter = 0
even_sum = 0

second_value = start_input + step_input
last_value = stop_input - step_input

iteration = range(start_input, stop_input, step_input)

for i in iteration:
    if i % 2 != 0:
        odd_counter += 1
    else:
        even_sum += i

print(f'2nd value in range = {iteration[1]}')
print(f'Last value in range = {iteration[-1]}')
print(f'odd_counter: {odd_counter}')
print(f'even_sum: {even_sum}')
