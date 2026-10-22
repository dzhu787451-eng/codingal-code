set1={1, 2, 3, 4}
set2={2, 8, 3, 2, 4, 3}
print("The original set is", set1)
print("The other original set is", set2)
set3=set1.intersection(set2)
print("The intersection of the two original sets is", set3)
set4=set1.union(set2)
print("The union of the two original sets is", set4)
set5=set1.difference(set2)
print("The difference in the two original sets is", set5)
set6=set1.symmetric_difference(set2)
print("The symmetric difference in the two original sets is", set6)