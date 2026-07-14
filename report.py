from ai_helper import ask_ai

def generate_report(student):

    prompt = f"""
You are an experienced AI Career Mentor.

Student Details:

Name: {student["Name"]}
Department: {student["Department"]}
Age: {student["Age"]}
Programming Knowledge: {student["Programming"]}
Career Goal: {student["Goal"]}
Area of Interest: {student["Interest"]}

Analyze this student and create a professional report.

Include:

1. Student Summary
2. Current Strengths
3. Current Weaknesses
4. Skills to Learn
5. Roadmap to Achieve the Career Goal
6. Recommended Projects
7. Certifications
8. Common Mistakes to Avoid
9. Daily Study Routine
10. Weekly Study Plan
11. Final Motivation

Format the report with clear headings and bullet points.
"""

    report = ask_ai(prompt)

    return report