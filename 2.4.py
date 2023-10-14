x = input("Введите строку: ")
ot = x.count('(')
zak = x.count(')')
if ot > zak:
    print("Не хватает", ot - zak, "закрывающей(их)")
elif ot < zak:
    print("Не хватает", zak - ot, "открывающей(их)")
else:
    print("Скобок поровну")