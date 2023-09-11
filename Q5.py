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
    
    def calcular_altura(self):
        return self._calcular_altura_recursiva(self.raiz)

    def _calcular_altura_recursiva(self, no):
        if no is None:
            return -1
        altura_esquerda = self._calcular_altura_recursiva(no.esquerda)
        altura_direita = self._calcular_altura_recursiva(no.direita)
        return max(altura_esquerda, altura_direita) + 1

    def travessia_inordem(self):
        valores = []
        self._travessia_inordem_recursiva(self.raiz, valores)
        return valores

    def _travessia_inordem_recursiva(self, no, valores):
        if no is not None:
            self._travessia_inordem_recursiva(no.esquerda, valores)
            valores.append(no.valor)
            self._travessia_inordem_recursiva(no.direita, valores)

# Teste da função de travessia inordem
arvore = ArvoreBinaria()
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(2)
arvore.inserir(4)
arvore.inserir(6)
arvore.inserir(8)

valores_inordem = arvore.travessia_inordem()
print("Travessia Inordem:", valores_inordem)
