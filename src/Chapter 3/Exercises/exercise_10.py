"""
Write a program that computes a user’s GPA on a 4 point scale. Each grade on
a 4 point scale is multiplied by the number of credits for that class. The sum of
all the credit, grade products is divided by the total number of credits earned.
"""

print("This program computes your GPA.\n"
      "Please enter your completed courses.\n"
      "Terminate your entry by entering 0 credits.")

credit = 1
credit_acc = 0
class_grade = 0
prod_acc = 0

while credit != 0:
    credit = int(input("Credits? "))
    credit_acc += credit
    if credit != 0:
        grade = input("Grade? ")
        if grade == "A":
            class_grade = 4 * credit
        elif grade == "A-":
            class_grade = 3.7 * credit
        elif grade == "B+":
            class_grade = 3.3 * credit
        elif grade == "B":
            class_grade = 3 * credit
        elif grade == "B-":
            class_grade = 2.7 * credit
        elif grade == "C+":
            class_grade = 2.3 * credit
        elif grade == "C":
            class_grade = 2 * credit
        elif grade == "C-":
            class_grade = 1.7 * credit
        elif grade == "D+":
            class_grade = 1.3 * credit
        elif grade == "D":
            class_grade = 1 * credit
        elif grade == "D-":
            class_grade = 0.7 * credit
        elif grade == "F":
            class_grade = 0 * credit
        prod_acc += class_grade

print("Your GPA is", prod_acc/credit_acc)
