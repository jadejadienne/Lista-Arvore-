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
    
    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(valor, self.raiz)
    
    def _inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)        
            else:
                self._inserir_em_nivel_recursivo(valor, no.direita)
                
    def travessia_pos_ordem(self):
        valores = []
        self._travessia_pos_ordem_recursiva(self.raiz, valores)
        return valores

    def _travessia_pos_ordem_recursiva(self, no, valores):
        if no is not None:
            self._travessia_pos_ordem_recursiva(no.esquerda, valores)
            self._travessia_pos_ordem_recursiva(no.direita, valores)
            valores.append(no.valor)


arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

valores_pos_ordem = arvore.travessia_pos_ordem()
print("Travessia Pós-ordem:", valores_pos_ordem)
