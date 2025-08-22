students = []   # list to store student records

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")
    
    students.append([roll, name, course, marks])
    print("✅ Student added successfully!\n")

def view_students():
    if len(students) == 0:
        print("No records found!\n")
        return
    
    print("\n--- Student Records ---")
    for s in students:
        print(f"Roll: {s[0]}, Name: {s[1]}, Course: {s[2]}, Marks: {s[3]}")
    print()

def menu():
    while True:
        print("==== Student Management System ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!\n")

if __name__ == "__main__":
    menu()
