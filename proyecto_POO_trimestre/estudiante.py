class Estudiante:
    def __init__(self, nombre, edad, grado, padres, contacto):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.padres = padres
        self.contacto = contacto

    def mostrar_estudiante(self):
        print(f'el nombre del estudiante es: {self.nombre}')
        print(f'la edad del estudiante es: {self.edad}')
        print(f'el grado que cursa el estudiante es: {self.grado}')
        print(f'los acudientes del estudiantes son: {self.padres}')
        print(f'El numero de contacto del acudiente es: {self.contacto}')
