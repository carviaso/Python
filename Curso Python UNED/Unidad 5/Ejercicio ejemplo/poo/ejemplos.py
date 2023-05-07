from autor import Autor
from edificio import Edificio
from estudiante import Estudiante
from animal import Animal
from gato import Gato
from jirafa import Jirafa
from cuadrado import Cuadrado
from figuraAbstracta import FiguraAbstracta
from clasePrivada import ClasePrivada

autor1 = Autor("David Fonseca","Costa Rica")

desc = autor1.descripcion()

print(desc)

estudiante1 = Estudiante()
estudiante1.nombre = "David"
estudiante1.cedula = "UNED-123"

#Sobrecarga
print(Animal().mostrarSonido())
print(Gato().mostrarSonido())
print(Jirafa().mostrarSonido())

#Abstraccion
cuadro = Cuadrado();
cuadro.lado = 5
print("Area del cuadrado: ",cuadro.calcularArea())
print("Perimetro del cuadrado: ", cuadro.calcularPerimetro())

#figura = FiguraAbstracta()

edificio1 = Edificio()
edificio1.areaDePiso = 2;

cp = ClasePrivada()
cp.setNombre("David")

gato2 = Gato()
gato3 = Gato()
jirafa2 = Jirafa()

def escucharAnimal(animal):
    print(animal.mostrarSonido())

escucharAnimal(gato2)
escucharAnimal(jirafa2)
escucharAnimal(gato3)

