class computadores:
    def __init__(self, ram, almacen, procesador,marca):
        self.ram = ram
        self.almacen = almacen
        self.procesador = procesador
        self.marca = marca 

    def encendido(self):
        print(f'tu {self.marca} esta encendido')

    def apagado(self):#==> se usa el self prar ahcer una autoreferencia, para poder de que el objeto acceda al metodo creado
        print(f'tu {self.marca} esta apagado')

macbook = computadores('8 gb','256 gb', 'chip m1', 'macbook air')

