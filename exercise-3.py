def remove_all_after(numbers, n):
    new_list = []
    for index, value in enumerate(numbers):
        new_list.append(value)
        if value == n:
            break
    return new_list

