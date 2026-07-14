from student import student_detail
from report import generate_report
from roadmap import generate_roadmap
from resources import recommended_resources
from project import recommend_projects
from menu import show_menu
from save_report import save_report
from loading import loading
from typing_effect import type_text
import time
student=None

def display_result(message,function,student):
    try:
        loading(message)
        start=time.time()
        result=function(student)
        end=time.time()
        response=end - start
        print(f"\n🐕 Response Generated in {response:.2f} seconds\n")
        type_text(result)

    except Exception as e:
        print("\n📉 Something went wrong!")
        print(e)

    
while True:
    choice = show_menu()

    if choice=="1":
        student=student_detail()
        print(student)
    elif choice=="2":
        if student:
            display_result("Generating Career Roadmap",generate_report,student)

        else:
            print("Enter student details")
    elif choice=="3":
        if student:
             display_result("Generating Learnin Resources",recommended_resources,student)
        else:
            print("Enter student details")
    elif choice=="4":
        if student:
             display_result("Generating Project Suggestions",recommend_projects,student)
        else:
            print("Enter student details")
    elif choice=="5":
        if student:
             display_result("Generating Complete Report ",generate_report,student)
        else:
            print("Enter student details")
    elif choice =="6":
        if student:
            loading("\nSaving Report\n....")
            filename=save_report(student)
            print(f"\nReport saved Succcessfully1\nLocation:{filename}")
        else:
            print("\nPlease enter student details first.")

    elif choice=="7":
        print("Thank you for using AI learning mentor")
        break
    else:
        print("\nInvalid Choice Please try again..")
