user_input = input("Enter row: ")
exit = 'x'
matrix = []
row_matrix = []
column_matrix = []
length_of_matrix = len(user_input.split(' '))

while user_input != exit:

    formatted_input = user_input.split(' ')
    if len(formatted_input) < length_of_matrix:
        while len(formatted_input) < length_of_matrix:
            formatted_input.append('0')

    temp_list = [int(i) for i in formatted_input]
    row_matrix.append(sum(temp_list))
    matrix.append(temp_list)
    user_input = input("Enter row: ")

if user_input == exit:
    transposed_mat = [list(i) for i in list(zip(*matrix))]
    for i in range(len(transposed_mat)):
        column_matrix.append(sum(transposed_mat[i]))
    output_matrix = [str(i).replace(',', '') for i in matrix]
    output_matrix = (str(output_matrix)
                     .replace(',', '\n')).replace("'", '')
    print(f'Example output: \n{output_matrix}')
    print(f'row sums: {row_matrix}')
    print(f'column sums: {column_matrix}')
    print(f'total sum: {sum(row_matrix)}')

