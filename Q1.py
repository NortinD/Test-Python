from sys import breakpointhook


a=int(input("t1 "))
b=int(input("T2 "))
h=int(input("T3 "))

if h<=b and h>a:
    print("Это нормально")
else:
   if h>b:
    print("Пересып")
   else:
        if h<a:
            print("Недосып")


    