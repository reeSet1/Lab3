# Файл основной части программы
from base import BaseClient
from methods import FriendsGet
from methods import UserGet

r = UserGet('53519062')
b = r.execute()
print(b)

f = FriendsGet(b);
a = f.execute()
print(a)
dates_list = sorted(list(a.keys()), reverse=True)
for i in dates_list:
    print(2016 - int(i), end=": ")
    print("#" * int(a[i]))
