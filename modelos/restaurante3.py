# criar um decorador @property
class Restaurante:
    restaurantes=[]
    
    def __init__(self,nome,categoria):
        self._nome=nome.title()
        self._categoria=categoria.upper()
        self._ativo=False
        
        Restaurante.restaurantes.append(self)
    

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    
    # 4 crianção de metodo que listas restaurantes
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'categoria'.ljust(20)} | {'status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')
    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    # metodo de objeto
    def alternar_estado(self):
        self._ativo=not self._ativo
    
    
# 2 criação de objetos
restaurante_praca=Restaurante('praça','Goumert')
restaurante_praca._nome='biqueira'
restaurante_praca.alternar_estado()
restaurante_pizza=Restaurante('pizza express','Italiana')




# 3 consumindo os objetos
# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))
# print('')


# print(restaurante_praca)
# print(restaurante_pizza)
# print('')

# 5 consumindo o metodo listar restaurante

Restaurante.listar_restaurantes()
