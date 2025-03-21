class A:
    def hablar(self):
        print('hola soy A ')
    
class B(A):
    def hablar(self):
        print(f'hablas desde B')

class C(A):
    def hablar(self):
        print(f'hablass desde C')

class D (B, C):
    pass

saludo = D()

saludo.hablar()