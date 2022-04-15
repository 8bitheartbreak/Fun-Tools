#exercise 1
"""list1 = [34, 54, 67, 89, 11, 43, 94]
print("OG List: " + str(list1))

var = 4
removedVar = list1.pop(var)

list1.insert(2, removedVar)
print(list1)

list1.append(removedVar)
print(list1)"""

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

count_dict = {}
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)