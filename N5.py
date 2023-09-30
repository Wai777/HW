x = float(input())
y = float(input())
if x > 0 and y > 0:
    print('1 четверть')
elif x > 0 and y < 0:
    print('4 четверть')
elif y == 0:
    print('Лежит на оси Оx')
elif x < 0 and y > 0:
    print('2 четверть')
elif x < 0 and y < 0:
    print('3 четверть')
elif x == 0:
    print('Лежит на оси Оу')
elif x == 0 and y == 0:
    print('Лежит в начале координат')
