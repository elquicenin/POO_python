class Cuenta:

    def __init__(self, titular, id_titular, numero_cuenta, saldo, fecha, tipo_cuenta, cupo):
        self.__titular = titular
        self.__id_titular = id_titular
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.__fecha = fecha
        self.__tipo_cuenta = tipo_cuenta
        self.__cupo = cupo

    def set_numero_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta
    
    def get_numero_cuenta(self):
        return self.__numero_cuenta 
    
    def get_id_titular(self):
        return self.__id_titular
    
    def visualizar_cuenta(self):
        print(f"**************************************************")
        print(f"Nombre del titular {self.__titular}")
        print(f"id del titular es: {self.__id_titular}")
        print(f"numero de cuenta {self.__numero_cuenta}")
        print(f"salgo de la cuenta {self.__saldo}")
        print(f"la fecha es {self.__fecha}")
        print(f"El tipo de cuenta es {self.__tipo_cuenta}")
        print(f"el cupo de la cuenta {self.__tipo_cuenta}")
        print(f"**************************************************")

    def retirar(self, monto):
        if self.__tipo_cuenta == 'ahorro':
            if self.__saldo - monto >= 10000:
                self.__saldo -= monto
                return True
        
            else: 
                return False
        
        elif self.__tipo_cuenta == 'corriente':
            if (self.__tipo_cuenta + self.__cupo) - monto >= 10000:
                self.__saldo -= monto
                return True
            else:
                return False
        
        else:
            return False
        
    def depositar(self, monto):
        if monto >= 10000:
            self.__saldo += monto
            return True
        return False
    
    def consultar(self):
        return self.__saldo
        


        