numero = int(input('Ingrese número :  '))
digitos = int(input('Ingrese digito :  '))
cantidad=0


def contarDigitos(numero, digitos):
   if numero >= 0 : 
    numero_text = str(numero)
    cantidad= numero_text.count(str(digitos))   
    print(f'Numero ingresado:  {numero} y dígito: {digitos}')
    print(f'Cantidad de {digitos} en número ingresado es : {cantidad}')
   else:
    print('Ingrese un numero entero')
    
contarDigitos(numero,digitos)

    



