def softuni_students(*name, **course_name):
    valid_course_students = {}
    invalid_course_students = set()
    for i in range(len(name)):
        if name[i][0] in course_name:
            valid_course_students[name[i][1]] = course_name[name[i][0]]
        else:
            invalid_course_students.add(name[i][1])
    sorted_valid = sorted(valid_course_students.items())
    result = []
    for name, course in sorted_valid:
        result.append(f"*** A student with the username {name} has successfully finished the course {course}!")
    if invalid_course_students:
        result.append(f"!!! Invalid course students:  {', '.join(sorted(invalid_course_students))}")

    return '\n'.join(result)


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))

