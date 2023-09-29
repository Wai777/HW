x=float(input())
y=float(input())
if x>0 and y>0:
    print('1 четверть')
if x>0 and y<0:
    print('4 четверть')
if y==0:
    print('Лежит на оси Оx')
if x<0 and y>0:
    print('2 четверть')
if x<0 and y<0:
    print('3 четверть')
if x==0:
    print('Лежит на оси Оу')
