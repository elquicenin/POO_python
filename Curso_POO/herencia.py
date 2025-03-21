#herencia de clases 

class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero


class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, curso, instituto):
        Persona().__init__(nombre , edad, genero)
        self.instituto = instituto
        self.curso = curso

samuel = Estudiante('Samuel', 18, 'masculino', 12,'SENA' )

print(samuel.nombre)