x=int(input())
y=int(input())
if x>0:
    if y>0:
        print('1 четверть')
    elif y<0:
        print('4 четверть')
    else:
        print('Лежит на оси Оу') 
elif x<0:
    if y>0:
        print('2 четверть')
    elif y<0:
        print('3 четверть')
    else:
        print('Лежит на оси Оу') 
else:
    print('Лежит на оси Ох')