user_input = int(input("Enter age: "))

if user_input < 0:
    print('Invalid age!')
elif user_input <= 7:
    print('Child ticket: 10$')
elif user_input <= 17:
    print('Teenager ticket: 15$')
elif user_input >= 18:
    salary_input = int(input("Enter salary: "))
    if salary_input < 0:
        print('Invalid salary!')
    elif salary_input <= 1000:
        print('Reduced adult ticket 1: 20$')
    elif salary_input <= 2000:
        print('Reduced adult ticket 2: 25$')
    else:
        print('Adult ticket: 30$')