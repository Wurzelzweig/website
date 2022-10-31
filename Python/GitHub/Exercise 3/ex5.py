options = {
    'exit': 'x', 'add': 'a', 'remove': 'r',
    'update': 'u', 'view': 'v'}
header = 'Welcome to Powerlifting Data Collector!\n'
info_text = '''
Available actions:
a - Add lifter
r - Remove lifter
u - Update lifter
v - View lifters
x - Exit the program'''

print(header, info_text)
user_input = input('Enter action: ')

dict_of_lifters = dict()
while user_input != options['exit']:
    # add
    if user_input == options['add']:
        name_of_lifter = input('Enter new lifter name: ')
        if name_of_lifter in dict_of_lifters.keys():
            print(f'Lifter "{name_of_lifter}" already exists!')
        else:
            dict_of_lifters.update({f'{name_of_lifter}':
                               {'squat': [],
                                'bench press': [],
                                'deadlift': []}})
    # remove
    if user_input == options['remove']:
        name_to_remove = input('Enter lifter name to remove: ')
        if name_to_remove not in dict_of_lifters.keys():
            print(f'Lifter "{name_to_remove}" does not exist!')
        else:
            dict_of_lifters.pop(name_to_remove)
    # update
    if user_input == options['update']:
        name_to_update = input('Enter lifter name to update: ')
        if name_to_update not in dict_of_lifters.keys():
            print(f'Lifter "{name_to_update}" does not exist!')
        else:
            update_lift = input(
                "Enter lift (one of 'squat', "
                "'bench press', 'deadlift'): ")
            if update_lift == 'squat':
                weight = input('Enter weight(s): ')
                weight = weight.split(' ')
                weight = [float(i) for i in weight]
                dict_of_lifters[f'{name_to_update}']['squat'].extend(weight)
            elif update_lift == 'bench press':
                weight = input('Enter weight(s): ')
                weight = weight.split(' ')
                weight = [float(i) for i in weight]
                dict_of_lifters[f'{name_to_update}']['bench press'].extend(weight)
            elif update_lift == 'deadlift':
                weight = input('Enter weight(s): ')
                weight = weight.split(' ')
                weight = [float(i) for i in weight]
                dict_of_lifters[f'{name_to_update}']['deadlift'].extend(weight)
            else:
                print('This option does not exist!')
    # view
    if user_input == options['view']:
        number_of_lifter = len(dict_of_lifters.keys())
        list_of_lifter_names = list(dict_of_lifters.keys())
        view_of_lifter = '''\n{line}\nName: {name}\nsquat: {squat}\nbench press: {bench_press}\ndeadlift: {deadlift}'''
        list_of_lifter = [view_of_lifter.format(line='-' * 45, name=list_of_lifter_names[i],
                                                squat=dict_of_lifters[list_of_lifter_names[i]]['squat'],
                                                bench_press=dict_of_lifters[list_of_lifter_names[i]]['bench press'],
                                                deadlift=dict_of_lifters[list_of_lifter_names[i]]['deadlift'])
                                                for i in range(number_of_lifter)]

        print(''.join(list_of_lifter))

    # invalid action
    if user_input not in options.values():
        print(f"Invalid action '{user_input}'. Try again!")

    # infotext
    print(info_text)
    user_input = input('Enter action: ')

# close prg
if user_input == options['exit']:
    print('Bye!')
