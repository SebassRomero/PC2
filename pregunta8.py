
def factorial(numero):
    if numero < 0:
        print('El números NO puede ser negativos')
    elif numero == 0 or numero == 1:
        return 1
    else:
        fact = 1
        for i in range(2, numero + 1):
            fact = fact*i
        print(f'El factorial de {numero} es {fact}')
    
numero = int(input('Ingrese número: '))
    
factorial(numero)