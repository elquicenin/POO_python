class Socio:
    def __init__(self, codigo, nombre, telefono, domicilio):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio
        
    def mostrar_socio(self):
        print(f'nombre: {self.nombre}')
        print(f'codio: {self.codigo}')
        print(f'telefono: {self.telefono}')
        print(f'domicilio: {self.domicilio}')