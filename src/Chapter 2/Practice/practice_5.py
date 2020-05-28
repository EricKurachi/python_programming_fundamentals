"""
Write a program that determines whether you can run for president.
To run for president the constitution states: No Person except a natural
born Citizen, or a Citizen of the United States, at the time of the Adoption
of this Constitution, shall be eligible to the Office of President; neither shall
any Person be eligible to that Office who shall not have attained to the Age of
thirty five Years, and been fourteen Years a Resident within the United States
[7]. Ask three questions of the user and use the guess and check pattern to
determine if they are eligible to run for President.
"""

naturalness = input("Please enter your citizenship: ")
age = int(input("Please enter your age: "))
residence_time = int(input("Please enter for how many years did you live in the US: "))

status = "you are eligible to run for President of the USA"

if naturalness != 'American':
    status = "you are not eligible to run for President of the USA"
if age < 35:
    status = "you are not eligible to run for President of the USA"
if residence_time < 14:
    status = "you are not eligible to run for President of the USA"

print(status)
