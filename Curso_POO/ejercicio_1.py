class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print('estudiando ando....')

nombre = input('ingresa tu nombre: ')
edad = input('ahora dame tu edad: ')
grado = input('En que grado te encuentras: ')

estudiante_1 = Estudiante(nombre, edad, grado)

print(f"""Datos del estudiante 
        Nombre = {estudiante_1.nombre}
        Edad = {estudiante_1.edad}
        Grado = {estudiante_1.grado}
""")

estudiar = input('que estas haciendo en este momento: ')
if estudiar.lower() == 'estudiando poo':
    print('eres un genio guacho')