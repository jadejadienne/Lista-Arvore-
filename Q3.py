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
                
    def buscar(self, valor):
        if self._buscar_recursivo(valor, self.raiz):
            return print('O número digitado está na árvore!')
        else:
            return print('O número digitado não está na árvore!')
    
    def _buscar_recursivo(self, valor, no):
        if no is None:
            return False
        if valor == no.valor:
            return True
        elif valor < no.valor:
            return self._buscar_recursivo(valor, no.esquerda)
        else:
            return self._buscar_recursivo(valor, no.direita)

# Exemplo de uso:
arvore = ArvoreBinaria()
arvore.inserir(10)
arvore.inserir(5)
arvore.inserir(15)
arvore.inserir(3)
arvore.inserir(7)

arvore.buscar(7)  
arvore.buscar(20)  
