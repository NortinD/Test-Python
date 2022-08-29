
a=int(input())
b=str(input())
c=int(input())
if b==('+'):
    print (a+c)
if b==('-'):
    print(a-c)

if b==('/') and c!=0:
    print(a/c)
elif c==0:
    print('Деление на 0!')
if b==('*'):
    print(a*c)
if b==('mod'):
    print(a%c)
if b==('pow'):
    print(a**c)
if b==('div'):
    print(a//c)

