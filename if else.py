a= int(input("Число "))
b= int(input("Делить на "))
if b != 0:
    print (a/b)
else: 
    print("Деление не возможно")
    b=int(input("Введите не нулевое значение "))
    if b==0:
        print("Не верно")
    else:
        print(a/b)
