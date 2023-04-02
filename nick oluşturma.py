import random

def nickOlusturucu():
    first = input("Kullanmak istediğin 10 başlık gir (virgülle ayrılmış): ").split(',')
    second = input("Kelimelere eklenecek 10 ek giriniz (virgülle ayrılmış): ").split(',')
    nicks = []
    for i in range(10):
        nicks.append("{}{}".format(random.choice(first),random.choice(second)))
    return nicks

for nick in nickOlusturucu():
    print(nick)
