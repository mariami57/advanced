def students_credits(*student_info):
    diyan_credits = {}
    credits_sum = 0
    result = ""
    for course in student_info:
        course_info = course.split("-")
        points_ratio = int(course_info[3]) / int(course_info[2])
        student_credits = int(course_info[1]) * points_ratio
        diyan_credits[course_info[0]] = student_credits
        credits_sum += student_credits
    if credits_sum >= 240:
        result += f"Diyan gets a diploma with {credits_sum:.1f} credits.\n"

    else:
        diff = 240 - credits_sum
        result += f"Diyan needs {diff:.1f} credits more for a diploma.\n"

    sorted_dyan_credits = sorted(diyan_credits.items(), key=lambda x: -x[1])
    for subject, score in sorted_dyan_credits:
        result += f"{subject} - {score:.1f}\n"
    return result


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)


