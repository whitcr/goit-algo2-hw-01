def find_min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))
    
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])
    
    return min(left_min, right_min), max(left_max, right_max)

array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
result = find_min_max(array)
print("Мінімум:", result[0], "Максимум:", result[1])
