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
                
    def travessia_pre_ordem(self):
        valores = []
        self._travessia_pre_ordem_recursiva(self.raiz, valores)
        return valores

    def _travessia_pre_ordem_recursiva(self, no, valores):
        if no is not None:
            valores.append(no.valor)
            self._travessia_pre_ordem_recursiva(no.esquerda, valores)
            self._travessia_pre_ordem_recursiva(no.direita, valores)

# Teste da função de travessia pré-ordem
arvore = ArvoreBinaria()
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(2)
arvore.inserir(4)
arvore.inserir(6)
arvore.inserir(8)

valores_pre_ordem = arvore.travessia_pre_ordem()
print("Travessia Pré-ordem:", valores_pre_ordem)
