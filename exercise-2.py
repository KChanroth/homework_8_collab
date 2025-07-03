def index_power(numbers, n):
    if n > len(numbers) - 1:
        return -1 
    else:
        return pow(numbers[n], n)
    
