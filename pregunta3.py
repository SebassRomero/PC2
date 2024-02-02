lista_numeros = []
par =0
impar =0
while True :
    preguntar = input('¿Desea ingresar un número?: ').lower()
    if preguntar == 'SI'.lower() : 
        numero = int(input('Ingrese número: '))
        lista_numeros.append(numero)
        if numero % 2==0 :
         par = par +1
        else:
         impar = impar +1
    elif preguntar == 'NO'.lower() :
       break

print(lista_numeros)
print(f'Cantidad de números pares son: {par}')
print(f'Cantidad de números pares son: {impar}')