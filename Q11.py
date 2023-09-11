class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direito = None

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
            if no.direito is None:
                no.direito = No(valor)
            else:
                self._inserir_recursivo(valor, no.direito)

    def e_arvore_de_busca(self):
        return self._e_arvore_de_busca_recursiva(self.raiz, float('-inf'), float('inf'))

    def _e_arvore_de_busca_recursiva(self, no, minimo, maximo):
        if no is None:
            return True
        
        if not minimo < no.valor < maximo:
            return False

        return (self._e_arvore_de_busca_recursiva(no.esquerda, minimo, no.valor) and
                self._e_arvore_de_busca_recursiva(no.direito, no.valor, maximo))

arvore = ArvoreBinaria()
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(2)
arvore.inserir(4)
arvore.inserir(6)
arvore.inserir(8)

e_arvore_de_busca = arvore.e_arvore_de_busca()
print("É uma árvore de busca válida:", e_arvore_de_busca)
