n = int(input('digite um numero para saber tabuada dele:'))
print(f'a tabuada do numero {n} é: ')
for c in range(1,n+1):
    r = n * c
    print(f'{n} X {c} = {r}')
