from estudiante import Estudiante


class Institucion_INEM:

    def __init__(self):
        self.estudiantes = []
        self.grados  =  []

    def buscar_estudiantes(self, nombre):
        for i in range(len(self.estudiantes)):
            if self.estudiantes[i].nombre == nombre:
                return i
        return -1
    
    def agregar_estudiante(self,estudiante):
        if self.buscar_estudiantes(estudiante.nombre) == -1:
            self.estudiantes.append(estudiante)
            return True
        return False
