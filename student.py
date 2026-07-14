def student_detail():
    print("\nEnter Student Details")

    student={
        "Name":input(" Enter your name "),
        "Department":input(" Enter your Department "),
        "Age":int(input( " Enter your age ")),
        "Programming":input(" Enter your programming knowledge "),
        "Goal":input(" What is your career goal ? "),
        "Interest":input(" What is area of interest" )
    }
    return student