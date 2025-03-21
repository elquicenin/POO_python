#herencia de clases 

class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

class Pasion:
    def __init__(self, pasion):
        self.pasion = pasion
        

    def mostrar_pasion(self):
        return (f'mi pasion es {self.pasion}')
        
        
class Estudiante(Persona,Pasion):
    def __init__(self, nombre, edad, genero, curso, instituto,pasion):
        Persona.__init__(self, nombre , edad, genero)
        Pasion.__init__(self, pasion)
        self.instituto = instituto
        self.curso = curso

    def present(self):
        print (f'hola soy {self.nombre}, {super().mostrar_pasion()} y trabajo en el {self.instituto}')


#herencia multiple de la clase persona 

samuel = Estudiante('Samuel', 18, 'masculino', 12,'SENA','teologia' )

# print(f'mi nombre es {samuel.nombre} y tengo {samuel.edad} años y me gusta mucho la {samuel.pasion} ')

print(samuel.present())