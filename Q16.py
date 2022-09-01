s = input()
x=1
j=len(s)-1
i=0
e=0
while i<j:
    if s[i]!=s[i+1]:
        i+=1
        e+=[1]+str(i)
    else:
        i=2
   
print (e)


