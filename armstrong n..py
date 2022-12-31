#wap to check whether the no. is armstrong no. or not
n=int(input("enter a 3 digit no."))
x=n
s=0
while n!=0:
    t=n%10
    s=s+t**3
    n=n//10
if s==x:
    print("number is armstrong")
else:
    print("number is not armstrong")
