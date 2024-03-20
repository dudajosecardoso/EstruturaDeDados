class Lista:
    def __init__(self, info=None):
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


def lista_vazia(lst):
    return lst is None


def lista_busca(lst, valor):
    atual = lst
    while atual is not None:
        if atual.info == valor:
            return atual
        atual = atual.prox
    return False

def lista_retira(lst, valor):
    anterior = None
    atual = lst

    while atual is not None:
        if atual.info == valor:
            if anterior is None:  
                lst = atual.prox
            else:
                anterior.prox = atual.prox
            break
        anterior = atual
        atual = atual.prox

    return lst

def lista_comprimento(lst):
    comprimento = 0
    atual = lst
    while atual is not None:
        comprimento += 1
        atual = atual.prox
    return comprimento

def ultimo(lst):
    if lst is None:
        return None
    atual = lst
    while atual.prox is not None:
        atual = atual.prox
    return atual

def lista_insere_final(lst, valor):
    if lst is None:
        return Lista(valor)
    atual = lst
    while atual.prox is not None:
        atual = atual.prox
    atual.prox = Lista(valor)
    return lst


def lista_retira_ant(lst, v):
    anterior = None
    atual = lst
    while atual is not None:
        if atual.prox is not None and atual.prox.info == v:
            if anterior is None:
                lst = atual.prox
            else:
                anterior.prox = atual.prox
            break
        anterior = atual
        atual = atual.prox
    return lst


def concatena(lst1, lst2):
    if lst1 is None:
        return lst2
    atual = lst1
    while atual.prox is not None:
        atual = atual.prox
    atual.prox = lst2
    return lst1
    
def main():
    lst = cria_lista()
    lst = insere_lista(lst, 50)
    lst = insere_lista(lst, 60)
    lst = insere_lista(lst, 70)
    lst = insere_lista(lst, 80)

    print("Lista:")
    lista_imprime(lst)

    valor_a_retirar = 60
    lst = lista_retira(lst, valor_a_retirar)

    print(f"\nLista depois de retirar o elemento {valor_a_retirar}:")
    lista_imprime(lst)

    print("Comprimento da lista:", lista_comprimento(lst))
    
    print("Último nó da lista:", ultimo(lst).info if ultimo(lst) is not None else None) # Corrigido
    lst = lista_insere_final(lst, 90)
    print("Lista depois de inserir 90 no final:")
    lista_imprime(lst)
    
    
    lst = lista_retira_ant(lst, 70)
    print("Lista após remover o elemento anterior a 70:")
    lista_imprime(lst)

    
    lst2 = cria_lista()
    lst2 = insere_lista(lst2, 100)
    lst2 = insere_lista(lst2, 110)
    lst2 = insere_lista(lst2, 120)

    print("\nSegunda lista:")
    lista_imprime(lst2)

    
    print("\nLista após concatenar com a segunda lista:")
    lst = concatena(lst, lst2)
    lista_imprime(lst)
    
main()
