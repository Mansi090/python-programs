'''d1={}
print(d1)

d1={1:'abc',2:'def'}


d2={'emp1':['mansi dixit',45678678],'emp2':['abhi',2345656]}
print(d2)

print(d1[1])
print(d2['emp2'])

print(d1.get(1))
print(d2.get('emp1'))
print(d1.get(56))

for k,v in d2.items():
    print(k,'=',v)


list1=[10,20,30,40,50,60]
list2=['abc','def','rtf','hui']
d1=dict(zip(list1,list2))

data1=input('data1:')
list1=data1.split()

data2=input('data2:')
list2=data2.split()

d2=dict(zip(list1,list2))
print(d2)


data1=input('data1:')
list1=data1.split()

data2=input('data2:')
list2=data2.split()
d1={}
if len(list1)==len(list2):
    for i in range(len(list1)):
        d1[list1[i]]=list2[i]
    print(sorted(d1.items()))
else:
    print("length should be equal")


data1=input('data1:')
list1=data1.split()

data2=input('data2:')
list2=data2.split()

d2=dict(zip(list1,list2))
print(d2)
a=input("enter key: ")
if a in d2:
    print(d2[a])
else:
    print("value does not exist")
 

data1=input('data1:')
list1=data1.split()

data2=input('data2:')
list2=data2.split()

d2=dict(zip(list1,list2))
for x in d2:
    print(x,d2[x])
'''

d1=[1:'abc',2;'def',3:'ghi',4:'jkl']





























