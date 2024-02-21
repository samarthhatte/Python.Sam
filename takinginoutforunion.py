def add_lists_using_union(list1, list2):
    # Convert lists to sets and perform union
    result_set = set(list1).union(set(list2))

    # Convert the result back to a list 
    result_list = list(result_set)

    return result_list


input_list1 = input("Enter elements for the first list (comma-separated): ")
input_list2 = input("Enter elements for the second list (comma-separated): ")

list1 = [int(x) for x in input_list1.split(',')]
list2 = [int(x) for x in input_list2.split(',')]
list3 = []

for element1 in list1:
    for element2 in list2:
        if element1 == element2:
            list3.append(element1)


result = add_lists_using_union(list1, list2)
uncommnelents = result - list3
print("Resulting List:", list3)
print("Uncommn elents: ",uncommnelents)