#to count no. which are divisble by 3 and 5
n=int(input("enter a no. :"))
i=1
count=0
while i<=n:
    if i%3==0 and i%5==0:
        count=count+1
    i=i+1
print("count is",count)
