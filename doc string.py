#working of docstring
def add(a,b):
    ''' author : nfvuj[ernogrv
date of creation: 09-11-2022
this function will add two nos'''
    return a+b
print(add.__doc__)
print("sum is",add(12,34))
