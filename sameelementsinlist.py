def add_lists_using_union(list1, list2):
    # Convert lists to sets and perform union
    result_set = set(list1).union(set(list2))

    # Convert the result back to a list
    result_list = list(result_set)

    return result_list

input_list1 = int(input("Enter elements for the first list (comma-separated): "))
input_list2 = int(input("Enter elements for the second list (comma-separated): "))


list1 = [int(x) for x in input_list1.split(',')]
list2 = [int(x) for x in input_list2.split(',')]
list3 = []



result = add_lists_using_union(list1, list2)
print("Resulting List:", result)
print("Common Elements:", list3)
