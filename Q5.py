
a=float(input())
c=float(input())
b=str(input())

if b==('+'):
    print (a+c)
if b==('-'):
    print(a-c)
if b==('/'): 
    if c!=0:
        print(a/c)
    elif c==0:
        print('Деление на 0!')
if b==('*'):
    print(a*c)
if b==('mod'):
    if c!=0:
        print(a%c)
    elif c==0:
        print('Деление на 0!')
if b==('pow'):
    print(a**c)
if b==('div'):
    if c!=0:
        print(a//c)
    elif c==0:
        print('Деление на 0!')

