
def ingresar_alumno():
    nombre = input('Ingrese el nombre del alumno: ')
    notas = []
    
    for i in range(3):
        nota = float(input(f'Ingrese la calificación {i + 1} del alumno {nombre}: '))
        notas.append(nota)
    
    alumno = {'Alumno': nombre, 'Notas': notas}
    return alumno


listado = []

n = int(input('Ingrese la cantidad de alumnos : '))

for i in range(n):
    alumnos = ingresar_alumno()
    listado.append(alumnos)
print('\nListado de alumnos : ')
print(listado)

