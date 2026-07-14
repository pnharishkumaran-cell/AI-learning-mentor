from ai_helper import ask_ai

def generate_roadmap(student):
    prompt =f"""
    You are an experienced Ai career mentor
    student details:
    name={student["Name"]}
    department={student["Department"]}
    age={student["Age"]}
    programming skills={student["Programming"]}
    career goal={student["Goal"]}
    Area of interest={student["Interest"]}

    Create a detailed and personalized roadmap for this student
    The roadmap should include
    12-month learning roadmap
    month 1-12
    skills to learn
    programming languages
    framework and tools
    best projects to build
    books to read daily study rooutine weekly learning pla
    interview preparation tips 
    internship preparation tips
    placement preparation 
    common mistakes to avoid
    final motivation

    Make the roadmap practical beginner friendly and easy to follow use
    headings,bullet points and proper formatting
    """
    roadmap=ask_ai(prompt)
    return(roadmap)
