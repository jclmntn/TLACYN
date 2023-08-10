import math
def two_crystal_balls(breaks: list[bool]) -> int:
    jump_amount = math.floor(math.sqrt(len(breaks)))
    
    for i in range(jump_amount, len(breaks), jump_amount):
        if breaks[i]:
            break
    
    i -= jump_amount
    for j in range(i, i + jump_amount):
        if breaks[j]:
            return j
        
    return -1