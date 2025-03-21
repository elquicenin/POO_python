from os import system 
import random
from datetime import date
from cuentas import Cuenta

class Banco:

    def __init__(self):
        self.__cuentas = []
        self.__numero_cuenta = []

    def pedir_datos_cuenta(self):
        try:
            system("cls")
            print('*****************************************')
            print('************ *CREAR CUENTA*  **********')
            print('*****************************************')
            print('*****************************************')
            titular = input('ingrese el nombre del titular de la cuenta: ')
            id_titular = input ('digite la identificacion del titular: ')
            num_cuenta = self.generar_numero_cuenta()
            saldo = int(input('Digite el salfdo inicial de la cuenta: '))
            fecha = date.today()
            num_cuenta = self.__numero_cuenta
            print(f"este es tu numero de cuenta {num_cuenta}")

            while True:
                print('*****************************************')
                print('*****        TIPO DE CUENTA         *****')
                print('*****************************************')
                print('********* 1. Ahorro *************')
                print('********* 2. Corriente *************')
                print('******************************************')
                
                try:
                    op_tipo_cuenta = int(input('ingrese la opcion del tipo de la cuenta: '))

                    if op_tipo_cuenta == 1:
                        tipo_cuenta = 'ahorro'
                        cupo = 0
                        break
                    
                    elif op_tipo_cuenta == 2:
                        tipo_cuenta = 'corriente'
                        

                        try:
                            cupo = int(input('Digite el cupo asignado'))
                            break
                        except ValueError:
                            print('Error el cupo debe ser un numero entero ')
                    
                    else:
                        print('*********************************') 
                        print('******Error opcion invalida******')
                        print('*********************************')
                        
                    cuenta = Cuenta (titular, id_titular, num_cuenta, saldo, fecha, tipo_cuenta, cupo)

                    if self.adicionar_cuenta(cuenta):
                        print('***************************************************')
                        print('*******Info, la cuenta se creo correctamente*******')
                        print('el numero de la cuenta es ', num_cuenta)
                        input()
                    else:
                        print('******************************************')
                        print('****Error la cuenta no se puede crear******')
                        input()
                except ValueError:
                    print('opcion invalida')
        except ValueError:
            print('Dato invalido')

    def generar_numero_cuenta(self):
        while True:
            numero = random.randint(1,9)
            if numero not in self.__numero_cuenta:
                self.__numero_cuenta.append(numero)
                break
            return numero
    
    def buscar_cuenta(self, num_cuenta):
        for i in range(len(self.__cuentas)):
            if num_cuenta == self.__cuentas[i].get_numero_cuenta():
                return i
        return -1
    
    def adicionar_cuenta(self, cuenta):
        pos = self.buscar_cuenta(cuenta.get_numero_cuenta())
        if pos == -1:
            self.__cuentas.append(cuenta)
            return True
        return False
    
    def pedir_datos_visualizar_cuenta(self):
            try:
                system('cls')
                print('************************************')
                print('********* VISUALIZAR CUENTA ********')
                print('************************************')
                num_cuenta = int(input('ingrese el numero de cuenta:' ))
                pos = self.buscar_cuenta(num_cuenta)

                if pos != -1:
                    self.__cuentas[pos].visualizar_cuenta()
                    input()

                else:
                    print('**********************************')
                    print('********Error numero de cuenta no existe*********')
            except ValueError:
                print('Error')

    def pedir_datos_retiro_cuenta(self):
        try:
            system('cls')
            print('****************************')
            print('*******  RETIROS ***********')
            num_cuenta = int(input('digite el monto a depositar: '))

            if self.buscar_cuenta(num_cuenta) != -1:
                monto = int(input('digite el monto a depositar'))

                if self.retirar_monto_cuenta(monto, num_cuenta):
                    print('*********************************')
                    print('****Info, retiro satisfactoriamente*******')
                    print('*********************************')
                
                else:
                    print('*******************************************')
                    print('******Error no se puede realizar el reito******')
            
            else:
                print('******************************************')
                print('**********el numero de cuenta no existe***********')
        except ValueError:
            print('ERROR|')
            input()

    def retirar_monto_cuenta(self, monto, num_cuenta):
        pos = self.buscar_cuenta(num_cuenta)
        if pos != -1:
            if self.__cuentas[pos].retirar(monto):
                return True
        return False
    
    def pedir_datos_deposito_cuenta(self):
        system('cls')
        print('******************************************')
        print('*********        DEPOSITOS     ***********')
        print('********************************************')
        num_cuenta = int(input('Digite el numero de la cuenta: '))

        if self.buscar_cuenta(num_cuenta) != -1:
            monto = int(input('Digite el monto a depositar'))

            if self.depositar_monto_cuenta(monto, num_cuenta):
                print('****************************************')
                print('*******info El deposito fue realizado de forma existosa ')

            else:
                print('****************************************')
                print('******No se puede realizar el deposto********')

        else:
            print('********************************')
            print('***** Error no se puede realizar el deposito')
    def depositar_monto_cuenta (self, monto, num_cuenta):
        pos = self.buscar_cuenta(num_cuenta)
        if pos != -1:
            if self.__cuentas[pos].depositar(monto):
                return True
        return False
    
    def mostar_saldo_cuenta(self):
        try:
            system('cls')

            print('*******************************************')
            print('****************SALDO CUENTA **************')
            print('********************************************')
            num_cuenta = int(input('ingrese el numero de cuneta: '))

            pos = self.buscar_cuenta(num_cuenta)
            if pos != -1:
                print('**********************************')
                print('**************el saldo de la cuenta es ' ,self.__cuentas[pos].consultar())
                input()


            else:
                print('*****************************************')
                print('****************la cuenta no existe***********')
        except ValueError:
            print('ERROR')
    
    def visualizar_cliente(self):
        system('cls')
        print('*******************************************************')
        print('***************** VISUALIZAR CLIENTE ******************')
        print('*******************************************************')
        id_titular = input('ingrese el documento del titular: ')

        pos_titular = self.buscar_cuenta(id_titular)
        if pos_titular !=1:
            print('*************************************')
            self.__cuentas[pos_titular].visualizar_clientes()
            print('*****************************************')
            input()

        else: 
            print('***************************************************')
            print('** **********EL TITULAR NO EXISTE******************')

    def buscar_cliente(self, id_titular):
        for i in range(len(self.__cuentas)):
            if id_titular == self.__cuentas[i].get_id_titular():
                return i
        return -1
    
    def mostrar_menu_principal(self): 
        while True:

            system('cls')
            print('****************************************')
            print(' *********       BANCO           *******')
            print('****************************************')
            print(' *********    MENU PRINCIPAL     *******')
            print('****   1.crear cuenta    ****'   )
            print('****   2. Visualizar cuemta    ****'   )
            print('****   3. Retirar    ****'   )
            print('****   4.  Depositar   ****'   )
            print('****   5.  Consultar saldo   ****'   )
            print('****   6. Consultar cliente    ****'   )
            print('****   0. SALIR    ****')

            try:
                
                op = int(input('seleciona una opcion: '))

                if op == 1:
                    self.pedir_datos_cuenta()
                elif op == 2:
                    self.pedir_datos_visualizar_cuenta()
                elif op == 3:
                    self.pedir_datos_retiro_cuenta()
                elif op == 4:
                    self.pedir_datos_deposito_cuenta()
                elif op == 5:
                    self.mostar_saldo_cuenta()
                elif op == 6:
                    self.visualizar_cliente()
                elif op == 0:
                    break
            except ValueError:
                print('dato invalido')

if __name__ == '__main__':
    banco = Banco()
    banco.mostrar_menu_principal()
