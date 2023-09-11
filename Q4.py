class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def __repr__(self):
        return '%s <-- %s --> %s' % (self.esquerda and self.esquerda.valor, self.valor, self.direita and self.direita.valor)
    
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)
    
    def _inserir_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)        
            else:
                self._inserir_recursivo(valor, no.direita)
    
    def altura(self):
        return self._altura_recursivo(self.raiz)

    def _altura_recursivo(self, no):
        if no is None:
            return -1
        altura_esquerda = self._altura_recursivo(no.esquerda)
        altura_direita = self._altura_recursivo(no.direita)
        return max(altura_esquerda, altura_direita) + 1


def calcular_altura_arvore(arvore):
    if arvore.raiz is None:
        return 0
    else:
        return arvore.altura()

# Teste da função
arvore = ArvoreBinaria()
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(2)
arvore.inserir(4)
arvore.inserir(6)
arvore.inserir(8)

altura = calcular_altura_arvore(arvore)
print("Altura da árvore:", altura)
