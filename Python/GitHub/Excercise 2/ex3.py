master_input = int(input("Enter a number to guess: "))
player_input = input('Enter number: ')
exit = 'exit'

while player_input != master_input:
    if player_input != exit:
        player_input = int(player_input)

    if player_input == exit:
        print('You lost!')
        break
    elif player_input == master_input:
        print('Congratulations!')
        break
    elif player_input < master_input:
        print('Your number is smaller.')
    elif player_input > master_input:
        print('Your number is bigger.')

    player_input = input('Enter number: ')
