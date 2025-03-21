from socio import Socio

class VideoClub:

    
    def __init__(self):
        self.socios = []
        self.peliculas = []

    def buscar_socio(self, codigo):
        for i in range (len(self.socios)):
            if self.socios == codigo:
                return i
        return -1
    
    def adicionar_socio(self, socio):
        if self.buscar_socio(socio.codigo) == -1:
            self.socios.append(socio)
            return True
        return False

                
    