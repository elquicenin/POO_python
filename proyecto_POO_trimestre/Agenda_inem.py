from estudiante import Estudiante
from INEM import Institucion_INEM
from os import system

class Menu:
    def __init__(self):
        self.inem = Institucion_INEM()

    def mostrar_menu(self):
        while True:
            print(f'******************************************')
            print(f'***************OPCIONES*******************')
            print(f'*****************INEM*********************')
            print(f'**********1. CREAR ESTUDIANTE **********')
            print(f'**********2. MOSTRAR ESTUDIANTE**********')
            print(f'*****************************************')
            print(f'*****************************************')
            print(f'*****************************************')
            print(f'**************0. SALIR ******************')
            try:
                op = input('ingrese una opcion: ')

                if op == '1':
                    self.agregar_estudiante()
                elif op =='2':
                    self.mostrar_estudiante()

                elif op =='0':
                    break
                else:
                    print('opcion invalida')

            except ValueError:
                print('Dato incorrecto')
            

    def agregar_estudiante(self):
        print('***********************************************')
        print('*********INGRESE DATOS DEL ESTUDIANTE**********')
        print('***********************************************')
        nombre = input('ingrese el nombre del estudiante: ')
        edad = input('ingrese la edad del estudiante: ')
        grado = input('ingrese el grado en que se encuentra el estudiante: ')
        padres = input('ingrese el nombre del acudiente: ')
        contacto = input('ingresa el numero de telefono de tu acudiente: ')
        student = Estudiante(nombre,edad,grado,padres,contacto)
        

        if self.inem.agregar_estudiante(student):
            print('**************************************')
            print('******** AGREGADO CON EXITO ************')
            print('**************************************')
        else:
            print('********************************************')
            print('***********EL ESTUDIANTE YA EXISTE**********')
            
    def mostrar_estudiante(self):
        nombre = input('Ingrese el nombre del estudiante a mostrar: ')
        estudiando = self.inem.buscar_estudiantes(nombre)
        if estudiando != -1:
            self.inem.estudiantes[estudiando].mostrar_estudiante()
        else:
            print('El estudiante no existe.')
        input("presione enter para continuar")

if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu()