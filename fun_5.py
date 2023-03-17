def liczby(c, *cyfry, j=0):
    print(c)
    print(cyfry)
    print(j)
    count = (len(cyfry))
    suma = 0
    print((type(cyfry)))
    for i in cyfry:
        suma += i
    print(f"Suma {suma}, srednia {suma / count}")


liczby(1, 5, j=34)
liczby(1, 5, 5, 6, 6, 7, 8, 9, 0, 99, 88, 77, j=10)


# 11:30
def connect(**opcje):
    print(opcje)
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080',
        'user': 'admin',
        'pass': '123456',
    }
    connect_param['pwd'] = opcje  # dodanie do słownika pary o kluczu pwd, wartosci ze zmiennej opcje
    print(connect_param)


connect(user='/home')
connect(root='/')
connect(root='/', user='/home')


def allparams(a, b, /, c=42, *args, d, **kwargs):  # / oddziela argumenty pozycyjne od nazwanych
    print('a,b', a, b)
    print('c', c)
    print('args', args)
    print('d', d)
    print('kwargs', kwargs)


allparams(1, 2, 3, 5, 6, 7, 8, 9, 0, d=19)
allparams(1, 2, 3, 5, 6, 7, 8, 9, 0, 999, d=19, f=14, g=19, zenek="a")
