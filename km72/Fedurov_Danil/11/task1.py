"""
    Дана функція підраховує макс. послідовність однакових елементів
    Args:
        list: list
        iterator: integer number
    Returns:
        int
    Raises:
        ValueError
    Examples:
        »>print(func([1, 1, 1, 2, 3], 0))
        3
        
        »>print(func([1, 1, s, 2, 2, 3], 0))
        Traceback (most recent call last):
            ...
        ValueError
    """

p = int(input("p="))
h = int(input("h="))
def func1(p):
    result = 0 
    for i in range(0,p):
        result = result + i
    return result
def func2(p,h):
    result = 1
    for z in range(p,h+1):
        result = result * z
    return result
print("Сума до числа p =",func1(p))
print("Произвидение p і h=",func2(p,h))
