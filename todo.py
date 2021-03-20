#!python3
from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []
    
    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possível IndexError
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluído)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now())
                status.append(f'(Vence em {dias} dias)')
        
        return f'{self.descricao}'+' '.join(status) 


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Lavar roupa', datetime.now())
    casa.add('Dar banho no cachorro', datetime.now() + timedelta(days=5))
    print(casa)
    for tarefa in casa:
        print(f'- {tarefa}')

    casa.procurar('Lavar roupa').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')

    mercado = Projeto('Compras de Mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate')
    print(mercado)
    for tarefa in mercado:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()
