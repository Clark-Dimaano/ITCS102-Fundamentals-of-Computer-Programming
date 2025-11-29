import os 
import json
os.system('cls')
print("DLL STUDENT INFORMATION SYSTEM")
print('==================================================')

student_info = {}
while True:
    print("Select from the following system")
    print("A - Add Student")
    print("B - Print all sudent info")
    print("C - Search Student")
    print("D - Delete Student Record")
    print("E - Edit Student Record")
    print("F - Export Data")
    print("G - Import Data")
    print("X - Exit System")

    choice = input("Input your choice --> ").lower().strip()

    if choice == 'a':
        print("ADD STUDENT RECORD")
        student_id = input("Input student number --> ")
        first_name = input("Input student First name --> ").upper()
        last_name = input("Input student Last name --> ").upper()
        course = input("Input student course --> ").upper()
        section = input("Input student section --> ").upper()
        email = input("Input student email --> ")

        student_info[student_id] = [first_name, last_name, course, section, email]
        os.system('cls')
        print("SAVED SUCCESSFULLY")
        continue

    elif choice == 'b':
        print("PRINTING STUDENT RECORD")
        
        for id,info in student_info.items():
                print(f"Student id {id} - Record {info}")

        
        continue 


    elif choice == 'c':
        print("SEARCH STUDENT RECORD")

        search_id = input("Input Student ID --> ").lower()

        for each_student in student_info.keys():
            print("\n\nRECORD FOUND")
            print("=====================================")
            if search_id in student_info.keys():
                for id,info in student_info.items():
                    print(f"STUDENT ID {id} - STUDENT INFO {info}")

            else:
                print("STUDENT RECORD NOT FOUND")
                break 

        continue 

    elif choice == 'd':

        search_id = input("Input Student ID --> ").lower()

        
        for each_student in student_info.keys():
            print("\n\nRECORD FOUND")
            print("=====================================")
            if search_id in student_info.keys():
                for id,info in student_info.items():
                    print(f"STUDENT ID {id} - STUDENT INFO {info}")
                
                    student_info.pop(search_id)
                    print("DELETED SUCCESSFULLY")
                    break
            else:
                print("INVALID ID, TRY AGAIN")
                continue
        continue 
    elif choice == 'e':
        search_id = input("Input Student ID --> ").lower()

        for each_student in student_info.keys():
            if search_id in student_info.keys():
                print(f"\n\nRECORD FOUND for {search_id}")
                print("=====================================")
                for id in student_info[search_id]:
                    print(f" --{id} ")

                print("======================================")
                print("EDIT STUDENT INFO")

                first_name = input("Input student First name --> ").upper()
                last_name = input("Input student Last name --> ").upper()
                course = input("Input student course --> ").upper()
                section = input("Input student section --> ").upper()
                email = input("Input student email --> ")

                student_info[search_id][0] = first_name
                student_info[search_id][1] = last_name
                student_info[search_id][2] = course
                student_info[search_id][3] = section
                student_info[search_id][4] = email
                print("DATA UPDATED SUCCESSFULLY")
                continue 

            else:
                print("NO RECORD FOUND")
                break

        continue 
    elif choice == 'f':
        print("EXPORT DATA")

        with open('student_info.json','w') as new_file:
            json.dump(student_info, new_file, indent=4)

        print("DATA EXPORTED SUCCESSFULLY")
        continue 
    elif choice == 'g':
        print("IMPORT DATA")

        with open('student_info.json','r') as new_file:
            imported_student = json.load(new_file)

        print("DATA IMPORTED SUCCESSFULLY")
       
    elif choice == 'x':
        print("System Exit")
        break

    else:
        print("Invalid choice, try again")