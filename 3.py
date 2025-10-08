from random import *
print(f'''Функции:
Бросить игральную кость - нажмите 1
Подбросить монетку - нажмите 2
Сгенирировать n чисел от a до b - нажмите 3
Сгенирировать n слов из списка - нажмите 4
Сгенирировать n слов из списка (без повторов) - нажмите 5
Закрыть программу - нажмите 0''')
d = {'1': 'Кол-во бросков', '2': 'Кол-во подбросов',
     '3': 'Введите кол-во чисел и диапазон', '4': 'Введите кол-во слов и список (дважды нажмите Enter, чтобы завершить список)',
     '5': 'Введите кол-во слов и список (дважды нажмите Enter, чтобы завершить список)'}
while True:
    f = input()
    if f == '':
        print('Нет')
    elif f not in '012345':
        print(f'''Введите цифру от 1 до 5
Чтобы завершить программу введите 0''')
    elif f == '0':
        break
    else:
        print(d[f])
        if f == '1':
            n = abs(int(input()))
            for _ in range(n):
                print(randint(1, 6), end = ' ')
            print()
        elif f == '2':
            n = abs(int(input()))
            for _ in range(n):
                print(choice(('О', 'Р')), end = ' ')
            print()
        elif f == '3':
            n, a, b = abs(int(input())), int(input()), int(input())
            for _ in range(n):
                print(randint(a, b), end = ' ')
            print()
        elif f == '4':
            n = abs(int(input()))
            lst = []
            while True:
                word = input()
                if word == '':
                    break
                else:
                    lst.append(word)
            for _ in range(n):
                print(choice(lst), end = ' ')
            print()
        else:
            n = abs(int(input()))
            lst = []
            while True:
                word = input()
                if word == '':
                    break
                else:
                    lst.append(word)
            if n > len(lst):
                print('Невозможно')
            else:
                shuffle(lst)
                print(*lst[:n])
                print()
