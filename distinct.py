def find_common_elements(list1, list2):
    # Convert lists to sets and find the intersection
    common_elements = set(list1).intersection(set(list2))-set(list1).union(set(list2))

    return list(common_elements)


# Example usage:
input_list1 = input("Enter elements for the first list (comma-separated): ")
input_list2 = input("Enter elements for the second list (comma-separated): ")

list1 = [int(x) for x in input_list1.split(',')]
list2 = [int(x) for x in input_list2.split(',')]

common_elements = find_common_elements(list1, list2)

if common_elements:
    print("Common Elements:", common_elements)
else:
    print("No common elements found.")
