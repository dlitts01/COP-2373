
import csv


# This function enters student information and saves it to a CSV file.
def write_grades():
    number_of_students = int(input("How many students do you want to enter? "))

    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Write the header for the file.
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam3"])

        # Enter the information for each student.
        for student in range(number_of_students):
            print(f"\nStudent {student + 1}")

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\nGrades have been saved to grades.csv")


# This function reads the CSV file and displays the grades.
def read_grades():
    print("\nStudent Grades")
    print("-" * 65)

    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)

        # Display each row in columns.
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<12}{row[3]:<12}{row[4]:<12}")


# Main function runs both functions.
def main():
    write_grades()
    read_grades()


main()
