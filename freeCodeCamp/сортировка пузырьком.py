def merge_sort(my_list):

    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) // 2

    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    sorted_list = []
    
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


print(merge_sort([2, 4, 5, 1, 10, 4]))
