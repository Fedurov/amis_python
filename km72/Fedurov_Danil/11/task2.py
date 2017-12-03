
X = []
def sp(n):    
    if n > 0:
        X.append(input("Введіть елемент - "))     
        return sp(n - 1)   
    else:
        return X
n = int(input("Введіть кількість елементів вашого списку - "))
sp(n)    


def minList(X, i):    
    global min    
    if i < len(X) - 1:
        if min > X[i + 1]:    
            min = X[i + 1]
            return minList(l, i + 1)    
    else:
        return minList(l, i + 1)
    return min

i = int(0)
min = X[i]
print(minList(X, i))
