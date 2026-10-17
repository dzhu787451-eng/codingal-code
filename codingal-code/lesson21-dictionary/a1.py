# 1) Create a dictionary `student_data` where:
#    a) Each key is a student ID (like "id1", "id2", etc.)
#    b) Each value is another dictionary containing student details:
#       - name
#       - class
#       - subject_integration

# 2) Create an empty dictionary `result` to store only unique student entries.

# 3) Create an empty set `seen` to keep track of student detail combinations already added.

# 4) Use a `for` loop to iterate through `student_data.items()`:
#    a) `student_id` holds the key (student ID)
#    b) `details` holds the value (student’s info dictionary)

# 5) For each student, create a tuple `unique_key` using:
#    (name, class, subject_integration)
#    (This tuple acts like a signature to identify duplicates.)

# 6) Check if `unique_key` is already in the `seen` set:
#    a) If it is NOT present:
#       i) Add `unique_key` to `seen`
#       ii) Add the student entry to `result` using `result[student_id] = details`
#    b) If it is already present, skip it (duplicate student details).

# 7) Print the final `result` dictionary line by line:
#    a) Use a loop through `result.items()`
#    b) Print each student ID and its details in the format: key : value

student_data={"id1":{"name": "john", "class": "4", "subject_integration": "english, math, science"},
              "id2":{"name": "sarah", "class": "5", "subject_integration": "english, math, science"},
              "id3":{"name": "david", "class": "4", "subject_integration": "english, math, science"},
              "id4":{"name": "sarah", "class": "5", "subject_integration": "english, math, science"}}
result={}
seen_keys=[]
for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])
    print(unique_key)
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id]=details

print("The seen keys are:", seen_keys)
print("The result is:", result)