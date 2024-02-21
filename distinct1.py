def find_distinct_elements(list1, list2):
    # Find the union of the two lists
    distinct_elements = list(set(list1).union(set(list2)))

    return distinct_elements


# Example usage:
input_list1 = input("Enter elements for the first list (comma-separated): ")
input_list2 = input("Enter elements for the second list (comma-separated): ")

list1 = [int(x) for x in input_list1.split(',')]
list2 = [int(x) for x in input_list2.split(',')]

distinct_elements = find_distinct_elements(list1, list2)

if distinct_elements:
    print("Distinct Elements:", distinct_elements)
else:
    print("No distinct elements found.")
