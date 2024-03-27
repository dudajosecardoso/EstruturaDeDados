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
    terceira_lista = Lista(None)
    atual = terceira_lista
    while lst is not None and segunda_lista is not  None:
        atual.prox = lst
        lst = lst.prox
        atual = atual.prox
        
        atual.prox = segunda_lista
        segunda_lista = segunda_lista.prox
        atual = atual.prox
        
    if lst is not None:
        atual.prox = lst
        
    if segunda_lista is not None:
        atual.prox = segunda_lista
        
    return terceira_lista
    

def invert(lst):
    ant = None
    atual = lst
    while atual:
        aux = atual.prox
        atual.prox = ant
        ant = atual
        atual = aux
        
    lst = ant
    return lst
    
    
def main():
    lst = cria_lista()
    lst = insere_lista(lst,1)
    lst = insere_lista(lst,2)
    lst = insere_lista(lst,3)
    lst = insere_lista(lst,4)
    lst = insere_lista(lst,5)
    
    print("Lista original:")
    lista_imprime(lst)
    print()
    
    
    valueToRemove = 2
    print(f"Lista com o valor {valueToRemove} removido:")
    lst = retira_n(lst, valueToRemove)
    
    lista_imprime(lst)
    print()
    
    valorSepara = 4
    print(f"Lista separada no valor {valorSepara}:")
    segunda_lista = separa(lst, valorSepara)
    lista_imprime(lst)
    print()
    lista_imprime(segunda_lista)
    print()
    
    print("Lista junta de novo:")
    terceira_lista = merge(lst, segunda_lista)
    lista_imprime(terceira_lista)
    print()
    
    print("Lista invertida:")
    lst = invert(lst)
    lista_imprime(lst)
    print()
    
    
main()
