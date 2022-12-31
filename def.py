
'''def add():
    a,b=eval(input("enter the value of a and b"))
    c=a+b
    print("the sum is ",c)
add()


def add(a,b):
    c=a+b
    print("the sum is ",c)


add(32,34)
add(22,87)'''

'''def simple_interest():
    p,r,t=eval(input("enter the value of p ,r and t"))
    s=(p*r*t)/100
    print("simple interestn is",s)

simple_interest()'''




'''def simple_interest(p,r,t):
    s=(p*r*t)/100
    print("simple interestn is",s)

simple_interest(2000,43,67)'''


def greatest():
    a=int(input("enter no."))
    b=int(input("enter no."))
    c=int(input("enter no."))
    if (a>b and a>c):
        print("greatest is",a)
    elif (b>a and b>c):
        print("greatest is ",b)
    else:
        print("greatest is ",c)
greatest()
    
    
