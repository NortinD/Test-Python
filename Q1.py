from sys import breakpointhook


a=int(input())
b=int(input())
h=int(input())

if (h<=b) and (h>=a) and (a<=b):
    print("Это нормально")
if (h>b) and (a<=b):
    print("Пересып")
if (h<a) and (a<=b):
    print("Недосып")


    