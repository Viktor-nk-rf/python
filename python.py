a=input().split() 
c=0

for i in range(len(a)): 
    if len(a[i])>c: 
        c=len(a[i])
    word=a[i]

print (word)