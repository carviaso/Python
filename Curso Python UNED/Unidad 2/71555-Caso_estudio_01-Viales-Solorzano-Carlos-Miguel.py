# Caso de estudio 1_Python_IC2023
'''
Universidad Estatal a Distancia (UNED)
Código 71555 - PROGRAMACIÓN BÁSICA CON PYTHON - IC2023
Unidad 2 - Caso de Estudio 1
Estidiante: Carlos Miguel Viales Solórzano
Cédula: 205100311

Trabajo Unidad 2 Caso de estudio 1 _Python_IC2023

Referencias:
- https://www.geeksforgeeks.org/find-average-list-python/
'''

''' Para referencia de funcion en la pagina https://www.geeksforgeeks.org/find-average-list-python/'''


# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)


# Informacion del Programa del Case de estudio de la Unidad 2
print("Universidad Estatal a Distancia (UNED)")
print("Código 71555 - PROGRAMACIÓN BÁSICA CON PYTHON - IC2023")
print("----")
print("Estidiante: Carlos Miguel Viales Solórzano")
print("Cédula: 205100311")
print("----")
print("Unidad 2 - Caso de Estudio 1")
print("----")
print("Instituto educativo de su comunidad ")

# Consulta el número de estudiantes
numeroEstudiantes = int(input("Cantidad de estudiantes a registrar: "))
a = 1
notas = []
while a < numeroEstudiantes + 1:
    print("Estudiante Numero: ", a)
    nota = input("Digite la nota del estudiante es:")
    notas.append(int(nota))
    a = a + 1

print("")
print("--- Calculos ---")
print("-- Nota Promedio es: ", Average(notas))
print("-- Nota Minima es: ", min(notas))
print("-- Nota Maxima es: ", max(notas))

for contador, valor in enumerate(notas):
    print("Estudiante : ", contador, valor)

print(list(enumerate(notas)))
