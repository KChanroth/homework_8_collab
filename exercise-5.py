def reverse_ascending(numbers):
    new_list = numbers.copy()
    block = []
    final_iteration = []
    while len(new_list) != 0:
        count = 1
        for x in new_list:
            try:
                if x < new_list[new_list.index(x)+1]:
                    count += 1
                else:
                    break
            except:
                count += 1

        block.append(new_list[0:count])
        for x in new_list[0:count]:
            new_list.remove(x)
    for x in block:
        for y in x[::-1]:
            final_iteration.append(y)
    return final_iteration

assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
    10,
    7,
    5,
    4,
    8,
    7,
    2,
    3,
    1,
]
assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
assert list(reverse_ascending([])) == []