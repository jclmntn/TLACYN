def binary_search(array: list[int], x: int) -> bool:
    low = 0
    high = len(array)

    while low < high:
        mid = (high + low) // 2
        
        if array[mid] == x:
            return True
        elif array[mid] > x:
            high = mid
        else:
            low = mid + 1

    return False
