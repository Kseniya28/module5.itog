def show_field(b):
    print("  0 1 2")
    for i in range(len(field)):
        print(str(i)+" "+" ".join(field[i]))

def users_input(b,user):
    while True:
        place=input(f"Ходит {user} .Введите координаты:").split()
        if len(place)!=2:
            print('Введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not(x>=0 and x<3 and y>=0 and  y<3):
            print('Вышли из диапазона')
            continue
        if b[x][y]!='-':
            print('Клетка занята')
            continue
        break
    return x,y


def win (b, user):
    def check_line(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True
    for n in range(3):
        if check_line(b[n][0], b[n][1], b[n][2], user) or \
        check_line(b[0][n], b[1][n], b[2][n], user) or \
                check_line(b[0][0], b[1][1], b[2][2], user) or \
        check_line(b[2][0], b[1][1], b[0][2], user):
                         return True
    return False


def start(field):

    count=0
    while True:
        show_field(field)
        if count%2==0:
            user='x'
        else:
            user = 'o'
        if count<9:
            x, y = users_input(field,user)
            field[x][y] = user

        elif count==9:
            print ('Ничья')
            break
        if win(field,user):
            print(f"Выйграл {user}")
            break
        count+=1


field = [['-'] * 3 for _ in range(3)]

start(field)
