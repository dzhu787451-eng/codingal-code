# 1) Create input data (student_data):
#    a) A dictionary where each key is a student_id (id1, id2, ...).
#    b) Each value is another dictionary containing student details (name, class, subject_integration).

# 2) Create result storage:
#    a) result = {} will store only unique student entries.
#    b) seen_keys = [] will store the unique identity of each student already added.
#    - NOTE: A list is used here instead of a set, so membership checking is slower.

# 3) Traverse each student entry:
#    a) Loop through student_data items (student_id, details).

# 4) Create a unique key for duplicate checking:
#    a) unique_key is a tuple of (name, class, subject_integration).
#    b) This tuple represents the “identity” of a student record.

# 5) Check for duplicates and store only unique entries:
#    a) If unique_key is not in seen_keys:
#       - append unique_key to seen_keys
#       - store this student in result using student_id as key.
#    b) If unique_key already exists, skip (duplicate record).

# 6) Print the final unique dictionary:
#    a) Loop through result items.
#    b) Print each student_id and its details line by line.

test_dictionary={"codingal": 2, "is": 2, "best": 2, "for": 2, "coding": 1}
print("Original dictionary:", test_dictionary)
k=2
result=0
for key in test_dictionary:
    if test_dictionary[key]==k:
        result+=1

print("The frequency of k is:", result)
