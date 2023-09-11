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
                
    def encontrar_valor_maximo(self):
        return self._encontrar_valor_maximo_recursivo(self.raiz)

    def _encontrar_valor_maximo_recursivo(self, no):
        if no is None:
            return float('-inf')

        valor_max_esquerdo = self._encontrar_valor_maximo_recursivo(no.esquerda)
        valor_max_direito = self._encontrar_valor_maximo_recursivo(no.direita)
        
        return max(no.valor, valor_max_esquerdo, valor_max_direito)

# Teste da função para encontrar o valor máximo
arvore = ArvoreBinaria()
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(2)
arvore.inserir(4)
arvore.inserir(6)
arvore.inserir(8)

valor_maximo = arvore.encontrar_valor_maximo()
print("Valor Máximo na Árvore:", valor_maximo)
