s = input()
i=0
n=1
while i<len(s)-1:
    if s[i]==s[i+1]:
        n+=1            
        i+=1       
    else:
        print(s[i]+str(n),end='')
        i+=1            
        n=1
print(s[i]+str(n),end='')


   



