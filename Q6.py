import math

object=str(input())
if object==('треугольник'):
    a=int(input())
    b=int(input())
    c=int(input())
    p=((a+b+c)/2)
    S=(math.sqrt(p*(p-a)*(p-b)*(p-c)))
    print(S)
if object==('прямоугольник'):
    a=int(input())
    b=int(input())
    S=(a*b)
    print(S)