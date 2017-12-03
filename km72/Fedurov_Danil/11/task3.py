X = []
Y = []
def func1(n):   
    if n > 0:
        X.append(input("Введіть елемент - "))     
        return func1(n - 1)  
    else:
        return X
n = int(input("Введіть кількість елементів списку - "))
func1(n)    
def revers(n):    
    if n == 0:
        return Y
    else:
        Y.append(X[n - 1])    
        return revers(n - 1)
revers(n)    
print(X, "Початковий список")
print(Y, "Перевернутий список")
