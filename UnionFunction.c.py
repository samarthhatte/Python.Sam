def add_lists_using_union(list1, list2):

    result_set = set(list1).union(set(list2))


    result_list = list(result_set)

    return result_list



list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = add_lists_using_union(list1, list2)
print(result)
