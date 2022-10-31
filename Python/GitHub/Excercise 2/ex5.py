header = "Welcome to the Data Statistics!"

info_string = '''\nAvailable actions:
a - Add numbers
v - View statistics
x - Exit the program'''

print(header)
print(info_string)
user_input = input('Enter action: ')
quit = 'x'
add_number = 'a'
view_statistics = 'v'
cnt = 0
sum = 0
new_list = []
list_of_elements = [quit, add_number, view_statistics]

while user_input not in list_of_elements:  # catch invalid inputs
    print(f"Invalid action '{user_input}'. Try again!")
    print(info_string)
    user_input = input('Enter action: ')

while user_input != quit:
    temp_user_input = user_input  # variable for inner loop

    while user_input not in list_of_elements:  # catch invalid input
        print(f"Invalid action '{user_input}'. Try again!")
        print(info_string)
        user_input = input('Enter action: ')

    while temp_user_input == add_number:
        number_input = temp_user_input
        if temp_user_input == add_number:
            number_input = input("Enter number or 'x' when you are done: ")
            if number_input != quit:
                number_input = int(number_input)
                cnt += 1
                sum += number_input
                avg = sum / cnt
                new_list.append(number_input)
                new_list.sort()

            if number_input == quit:
                temp_user_input = number_input

    if user_input == view_statistics:
        if cnt == 0:
            print("No numbers have been entered yet!")
        else:
            print(f"Count: {cnt}")
            print(f"Sum: {sum}")
            print(f"Avg: {avg}")
            print(f"Min: {new_list[0]}")
            print(f"Max: {new_list[-1]}")

    print(info_string)
    user_input = input('Enter action: ')

print("Bye!")
