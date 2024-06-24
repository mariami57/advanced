n_students = int(input())

some_dict = {}
for _ in range(n_students):
    student, grade = input().split()
    grade_float = float(grade)
    if student not in some_dict:
        some_dict[student] = []
    some_dict[student].append(grade_float)

for name, value in some_dict.items():
    avg_grade = sum(value) / len(value)
    grades_as_str = [str(x) for x in value]
    print(f"{name} -> {' '.join ([f'{x:.2f}' for x in value])} (avg: {avg_grade:.2f})")
