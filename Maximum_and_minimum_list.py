num=int(input("enter the required number"))
n=[]
for i in range(num):
    i=int(input("enter the number"))
    n.append(i)
print(n)
print("value of maximum is",max(n))
print("value of manimum is",min(n))