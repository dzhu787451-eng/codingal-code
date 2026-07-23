# 1) Ask the student if they had a medical cause and store the answer in `medical_cause`.
#    (Also clean the input so it becomes either 'Y' or 'N'.)

# 2) If `medical_cause` is 'Y':
#    - Print that the student is allowed to attend the exam.

# 3) Otherwise (medical_cause is 'N'):
#    a) Ask for the student’s attendance percentage and store it in `atten`.
#    b) If `atten` is 75 or more:
#       - Print "Allowed"
#    c) Else:
#       - Print "Not allowed"

medical_condition=input("Do you have a medical condition? (Y/N) ")
attendance=int(input("Please enter your attendance number: "))
if medical_condition=="N":
    if attendance>=75:
        print("You are allowed to take the exam")
    else:
        print("You are not allowed to take the exam")
else:
    print("You are allowed to take the exam")

if medical_condition=="N" and attendance>=75:
    print("You are allowed to take the exam")
elif medical_condition=="Y":
    print("You are allowed to take the exam")
else:
    print("You are not allowed to take the exam")