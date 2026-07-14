from ai_helper import ask_ai

def recommend_projects(student):

    prompt = f"""
    You are an experienced AI Career Mentor.

    Student Details:

    Name: {student["Name"]}
    Department: {student["Department"]}
    Age: {student["Age"]}
    Programming Knowledge: {student["Programming"]}
    Career Goal: {student["Goal"]}
    Area of Interest: {student["Interest"]}

    Recommend projects suitable for this student.

    Include:

    1. Beginner Projects (5)
    2. Intermediate Projects (5)
    3. Advanced Projects (5)
    4. Technologies Required
    5. Difficulty Level
    6. Estimated Completion Time
    7. Skills Gained
    8. Which project should be built first?
    9. Which project is best for a resume?
    10. Final Advice

    Use proper headings and bullet points.
    """

    return ask_ai(prompt)