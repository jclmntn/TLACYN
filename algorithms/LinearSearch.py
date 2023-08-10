def linear_search(array: list[int], x:int) -> bool:
    for i, y in enumerate(array):
        if x == y:
           return True

    return False
