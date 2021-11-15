while True:
    nota = float(input().strip())
    if nota == str:
        print('Nota inválida')
    if 8.5 <= nota <=10:
        print('A')
        break
    elif 7.5 <= nota <=8.4:
        print('B')
        break
    elif 5.0 <= nota <=7.4:
        print('C')
        break
    elif 4.0 <= nota <5:
        print('D')
        break
    elif 0.0 <= nota <4:
        print('E')
        break
    else:
        print(f'Nota inválida.')
