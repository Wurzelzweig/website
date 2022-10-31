width = int(input("Enter width: "))
squat = float(input("Enter squat: "))
bench_press = float(input("Enter bench press: "))
deadlift = float(input("Enter deadlift: "))

hashtag = "#"
hyphen = '-'
total = squat + bench_press + deadlift

header = "# Powerlifting 2022W"
length_header = len(header)
diff_header = width - length_header
string_header = f"{header}{hashtag:>{diff_header}}"

var_squat = f"Maximum Squat:"
length_var_squat = len(var_squat)
diff_squat = width - length_var_squat - 2
string_squat = f"{var_squat}{squat:>{diff_squat}.1f}kg"

var_bench_press = f"Maximum Bench Press:"
length_var_bench_press = len(var_bench_press)
diff_bench_press = width - length_var_bench_press - 2
string_bench_press = f"{var_bench_press}{bench_press:>{diff_bench_press}.1f}kg"

var_deadlift = f"Maximum Deadlift:"
length_var_deadlift = len(var_deadlift)
diff_deadlift = width - length_var_deadlift - 2
string_deadlift = f"{var_deadlift}{deadlift:>{diff_deadlift}.1f}kg"

var_total = f"Total :"
length_var_total = len(var_total)
diff_total = width - length_var_total - 2
string_total = f"{var_total}{total:>{diff_total}.1f}kg"

print(hashtag*width)
print(string_header)
print(hashtag*width)
print(string_squat)
print(string_bench_press)
print(string_deadlift)
print(hyphen*width)
print(string_total)