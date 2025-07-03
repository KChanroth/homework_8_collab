#chunking_by([5, 4, 7, 3, 4, 5, 4], 3) == [[5, 4, 7], [3, 4, 5], [4]]
#chunking_by([3, 4, 5], 1) == [[3], [4], [5]]

def chunking_by(numbers, chunck):
    #check for any issue with the provided variables
    if len(numbers) <= 0:
        return "The list is empyt"
    if chunck <= 0:
        return "Please enter a number higher than '0'"
    elif isinstance(chunck, int) is False:
        return "Please enter a whole number"

    block = []
    last_block = []
    times = len(numbers)//chunck
    for y in range(times):
        block.append(numbers[0:chunck])
        for x in numbers[0:chunck]:
            numbers.remove(x)
    if len(numbers) != 0:
        for x in numbers:
            last_block.append(x)
        block.append(last_block)
    return block

print(chunking_by([3, 4, 5], 1))
