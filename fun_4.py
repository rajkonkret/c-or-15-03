def fun1(a):
    print("To jest fun1")

    def fun2():
        print("Euro")

    def fun3():
        print("Dolary")

    if a.upper() == "USD":
        return fun3
    else:
        return fun2


xFun1 = fun1("EUr")
print(type(xFun1))
xFun1()  # uruchom funkcje
