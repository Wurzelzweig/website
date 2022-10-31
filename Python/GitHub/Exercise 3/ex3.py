user_input = input('Enter string: ')
user_input = user_input.lower()

unique = set()
for i in user_input:
    for j in user_input:
        if i == j:
            cnt = 0
            cnt += 1
    if cnt == 1:
        unique.update(i)
counter_list = [user_input.count(i) for i in unique]
unique_list = list(unique)

new_dict = {}
max_cnt = len(unique_list) - 1
cnt = 0

while cnt < max_cnt:
    cnt += 1
    new_dict.update(new_dict.fromkeys(unique_list[cnt], counter_list[cnt]))

print(f'Example output: {new_dict}')
