from socio import Socio
from videoclub import VideoClub
from os import system

class Menu:
    def __init__(self):
        self.videoclub = VideoClub()
    
    def mostrar_menu_principal(self):
        while True:
            system("cls")
            print("+++++++++++++++++++++++++++++")
            print("++++++Videoclub Quiceno++++++")
            print("+++++++++++++++++++++++++++++")
            print("+++++++++++++++++++++++++++++")
            print("+++++++MENU PRINCIPAL++++++++")
            print("1. crear socio")
            print("2. listar socios")
            print("4. Modidificar socio")
            print("5. Eliminar socio")
            print("6. Listar peliculas")
            print("7. Mostrar peliculas")
            print("8. Eliminar pelicula")
            print("9. Alquilar pelicula")
            print("10. Listar peliculas alquiladas")
            print("0. Salir")
            print("+++++++++++++++++++++++++++++++")
            break
        try:

            op = (input('selecione una opcion: '))
            print("******************************")

            if op == '1':
                self.adicionar_socio()
            elif op == '2':
                self.listar_socio()
            elif op == '3':
                self.modificar_socio()
            elif op == '4':
                self.eliminar_socio()
            elif op == '5':
                self.listar_peliculas()
            elif op == '6':
                self.mostrar_peliculas()
            elif op == '7':
                self.eliminar_pelicula()
            elif op == '8':
                self.alquilar_pelicula()
            elif op == '9':
                self.listar_peliculas_alquiladas()
        except ValueError:
            print('Opciion invalidad')

    def adicionar_socio(self):
        system("cls")
        print("****************************************")
        print("************ADICIONAR SOCIO*************")
        print("****************************************")
        codigo = input('digite el codigo del socio: ')
        nombre = input('digite nombre del socio ')
        telefono = input('digite el telefono del socio: ')
        domicilio = input('Digite el domicilio del socio: ')
        socio = Socio(codigo,nombre,telefono,domicilio)

        if self.videoclub.adicionar_socio(socio):
            print('***********************************************')
            print('*****el socio fue almacenado existosamente*****')
            input()
        else:
            print('***********************************************')
            print('************* el socio ya existe *************')

if __name__ == '__main__':
    menu = Menu()
    menu.mostrar_menu_principal()