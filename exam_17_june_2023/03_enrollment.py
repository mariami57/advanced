def gather_credits(n_credits, *course_info):
    courses = []
    credits_collected = 0
    for course_name, course_credits in course_info:
        if n_credits > credits_collected:
            if course_name not in courses:
                courses.append(course_name)
                credits_collected += course_credits
        else:
            break

    if n_credits > credits_collected:
        return f"You need to enroll in more courses! You have to gather {n_credits - credits_collected} credits more."
    else:
        return f"""Enrollment finished! Maximum credits: {credits_collected}.
Courses: {', '.join(sorted(courses))}"""


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))


