import os
from report import generate_report
def save_report(student):
    report=generate_report(student)
    filename=f'reports/{student["Name"]}_AI_Report.txt'

    with open(filename,"w",encoding='utf-8') as file:
        file.write(report)

    return filename
