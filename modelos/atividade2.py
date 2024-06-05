# criar uma classe Restaurante

class Restaurante:
    restaurantes=[]
    
    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False
        Restaurante.restaurantes.append(self)
    

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    
    # crianção de metodo que listas restaurantes
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
    
    
    
    
# 2 criação de objetos
restaurante_praca=Restaurante('Praça','Goumert')

restaurante_pizza=Restaurante('Pizza Express','Italiana')


# 3 consumindo os objetos
print(vars(restaurante_praca))
print(vars(restaurante_pizza))
print('')


print(restaurante_praca)
print(restaurante_pizza)
print('')

# 5 consumindo o metodo listar restaurante

Restaurante.listar_restaurantes()




#atividade 1

class Carro:

     
     def __init__(self,modelo,cor,ano):
        self.modelo=modelo
        self.cor=cor
        self.ano=ano
        self.ativo=False
        Restaurante.restaurantes.append(self)
    