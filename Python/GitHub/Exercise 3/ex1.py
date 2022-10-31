user_input = input('Enter string: ')

islower_list, isupper_list, other_list = [], [], []
unique_set = set()

for i in user_input:

    if i.islower():
        islower_list.append(i)
    elif i.isupper():
        isupper_list.append(i)
    else:
        other_list.append(i)
    for j in user_input:
        if i == j:
            cnt = 0
            cnt += 1
    if cnt == 1:
        unique_set.update(i)

print(f'lowercase: {islower_list}')
print(f'uppercase: {isupper_list}')
print(f'other: {other_list}')
print(f'unique: {unique_set}')
