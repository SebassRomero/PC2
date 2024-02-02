texto = input('Ingrese texto:  ')

def omitir_vocales(cadena):
    vocales = 'aeiouAEIOU'
    resultado = ""

    for letra in cadena:
        if letra not in vocales:
            resultado += letra

    return resultado

resultado = omitir_vocales(texto)
print("Resultado: " + resultado)