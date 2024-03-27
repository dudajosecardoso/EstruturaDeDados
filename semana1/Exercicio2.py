class Lista:
    def __init__(self, info = None):
        self.info = info
        self.prox = None
        
def cria_lista():
    return Lista()
    
def insere_lista(lst, valor):
    novo = Lista(valor)
    novo.prox = lst
    return novo
    
def lista_imprime(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox
    
 
def retira_n(lst, valor):
    ant = None
    atual = lst
    while atual:
        if atual.info == valor:
            if ant:
                ant.prox = atual.prox
            else:
                lst = atual.prox
        else:
            ant = atual
        atual = atual.prox
    return lst

def separa(lst, valorSepara):
    atual = lst
    while atual is not None and atual.info != valorSepara:
        atual = atual.prox
        
    if atual is None:
        return None
        
    segunda_lista = atual.prox
    atual.prox = None
    
    return segunda_lista


def merge(lst, segunda_lista):
    

#4
#def invert(lst):
#    ant = None
 #   atual = lst
  #  while atual:
   #     aux = atual.prox
    #    atual.prox = ant
     #   ant = atual
      #  atual = aux
    #return lst
    
    
def main():
    lst = cria_lista()
    lst = insere_lista(lst,1)
    lst = insere_lista(lst,2)
    lst = insere_lista(lst,3)
    lst = insere_lista(lst,4)
    lst = insere_lista(lst,5)
    
    
    lista_imprime(lst)
    print()
    
    valueToRemove = 2
    lst = retira_n(lst, valueToRemove)
    
    lista_imprime(lst)
    print()
    
    valorSepara = 4
    segunda_lista = separa(lst, valorSepara)
    lista_imprime(lst)
    print()
    lista_imprime(segunda_lista)
    
    
main()
