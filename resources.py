from ai_helper import ask_ai

def recommended_resources(student):

    prompt = f"""
    You are an experienced AI Career Mentor.

    Student Details

    Name: {student["Name"]}
    Department: {student["Department"]}
    Age: {student["Age"]}
    Programming Knowledge: {student["Programming"]}
    Career Goal: {student["Goal"]}
    Area of Interest: {student["Interest"]}

    Recommend the best learning resources.

    Include:

    1. Best YouTube Channels
    2. Best Free Courses
    3. Best Paid Courses
    4. Best Websites
    5. Best Documentation
    6. Best Books
    7. GitHub Repositories
    8. Practice Websites
    9. Coding Challenge Websites
    10. AI Communities
    11. Discord Servers
    12. Reddit Communities
    13. Newsletters
    14. Podcasts

    Explain why each resource is useful.

    Format everything with headings and bullet points.
    """

    return ask_ai(prompt)