#2ème paatie:Récursivité


#b) la fonction récursive divinRec(a,b)
def divinRec(a, b):
    if a < b:
        return 0
    else:
        return 1 + divinRec(a - b, b)


#2.2
def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)
