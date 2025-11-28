#Credentials or Information of the users
users = {
    "Regodon": {"role": "student", "password": "02-2526-021093"},
    "Tahud": {"role": "student", "password": "02-2526-029290"},
    "Teacher": {"role": "teacher", "password": "1234"}
    
}

#Initial Grade output
grades = {
    "Regodon": {
    "project": 0, 
    "quiz": 0, 
    "assignment": 0, 
    "behavior": 0, 
    "exam": 0},
    "Tahud":{
    "project": 0, 
    "quiz": 0, 
    "assignment": 0, 
    "behavior": 0, 
    "exam": 0}
}

#List of request from students
grade_requests = []

#Main System
while True:
    #Log in System
    while True:
        print("\n=== LOGIN ===")
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Logged in as {role}")
            break
        else:
            print("Invalid credentials. Try again.\n")
    
    # Student Menu or Interface
    if role == "student":
        while True:
            print("\n--- Student Menu ---")
            print("1. View Grades")
            print("2. Request Grade")
            print("3. Logout")
            choice = input("Choose an option: ")
            
            if choice == "1":
                if username in grades:
                    g = grades[username]
                    cs = round(g["project"]*0.4 + g["quiz"]*0.3 + g["assignment"]*0.2 + g["behavior"]*0.1, 2)
                    
                    final_grade = round(cs*0.5 + g["exam"]*0.5, 2) 
                    
                    print(f"\nProject: {g['project']}, \nQuiz: {g['quiz']}, \nAssignment: {g['assignment']}, \nBehavior: {g['behavior']}, \nExam: {g['exam']}")
                    print(f"Class Standing: {cs}")
                    print("Status:", "Passed" if cs >= 50 else "Not Yet Passed")
                    print(f"\nFinal Grade: {final_grade}")
                    print("Status:", "Passed" if final_grade >= 50 else "Not Yet Passed")
                else:
                    print("No grades uploaded yet.")
            
            elif choice == "2":
                if username in grade_requests:
                    print("You have already requested your grade. Please wait for the teacher.")
                else:
                    grade_requests.append(username)
                    print("Grade request submitted.")

            
            elif choice == "3":
                print("Logging out...")
                break
            
            else:
                print("Invalid option.")

    # Teacher Menu or Interface
    elif role == "teacher":
        while True:
            print("\n--- Teacher Menu ---")
            print("1. View All Grades")
            print("2. View Grade Requests")
            print("3. Edit Student Grades")
            print("4. Logout")
            choice = input("Choose an option: ")
            
            if choice == "1":
                for student, g in grades.items():
                    cs = round(g["project"]*0.4 + g["quiz"]*0.3 + g["assignment"]*0.2 + g["behavior"]*0.1, 2)
                    
                    final_grade = round(cs*0.5 + g["exam"]*0.5, 2) 
                    
                    print(f"\nStudent: {student}")
                    
                    print(f"\nProject: {g['project']}, \nQuiz: {g['quiz']}, \nAssignment: {g['assignment']}, \nBehavior: {g['behavior']}, \nExam: {g['exam']}")
                    
                    print(f"Class Standing: {cs}, Status: {'Passed' if cs >= 50 else 'Not Yet Passed'} \nFinal Grade: {final_grade}, Status: {'Passed' if final_grade >= 50 else 'Not Passed'}")
            
            elif choice == "2":
                if grade_requests:
                    print("\nGrade Requests from Students:")
                    for r in grade_requests:
                        print("-", r)
                else:
                    print("No grade requests.")
            
            elif choice == "3":
                student = input("Enter student username to edit: ")
                if student in grades:
                    try:
                        grades[student]["project"] = float(input("Enter Project grade: "))
                        grades[student]["quiz"] = float(input("Enter Quiz grade: "))
                        grades[student]["assignment"] = float(input("Enter Assignment grade: "))
                        grades[student]["behavior"] = float(input("Enter Behavior grade: "))
                        grades[student]["exam"] = float(input("Enter Exam grade: "))
                        print("Grades updated.")
                    except ValueError:
                        print("Invalid input. Please enter numerical values for grades.")
                else:
                    print("Student not found.")
            
            elif choice == "4":
                print("Logging out...")
                break