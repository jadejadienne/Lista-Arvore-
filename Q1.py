class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def __repr__(self):
        esq = self.esquerda.valor if self.esquerda else None
        dir = self.direita.valor if self.direita else None
        return f'{esq} - {self.valor} - {dir}'
    
no1 = No(5)
no2 = No(3)
no3 = No(7)

no1.esquerda = no2
no1.direita = no3

print(no1)
