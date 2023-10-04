from conect import Conexao as Conn

db = Conn(database='database.db', username= 'admin', password= '1234')


class Mercadoria:
    def __init__(self, nome:str, temperatura:int, comissao:float, fundofunil:str, pesquisas:str, paginavenda:str) -> None:
        self.nome = nome
        self.temperatura = temperatura
        self.comissao = comissao
        self.fundofunil = fundofunil
        self.pesquisas = pesquisas
        self.paginavenda = paginavenda

escolha = input("Deseja manipular de qual modo?").lower()
while True:
    if escolha == 'cadastrar':

        nome = input("Digite o nome do produto:")
        temperatura = input("Digite o temperatura do produto:")
        comissao = input("Digite o comissao do produto:")
        fundofunil = input("Digite se o produto é fundo de funil:")
        pesquisas = input("Digite a quantidade pesquisas do produto:")
        paginavenda = input("Digite se o produto tem pagina de vendas:")
        db.inserir_dado(nome = nome, temperatura = temperatura, comissao = comissao, fundofunil = fundofunil, pesquisas= pesquisas, paginavenda =  paginavenda)

    elif escolha == 'consultar':
        while True:
            produto = input("Qual produto você deseja consultar?")
            print(db.consultar_dado(produto))
            cont = input('Deseja consultar mais algum produto?(s/n)').lower()
            if cont == 'n':
                False

    elif escolha == 'consultar tudo':
        print(db.consultar__tabela)
    
    elif escolha == 'sair':
        break

    else:
        print('''Digite uma entrada válida.
            cadastrar.
            consultar.
            consultar tudo.
            sair.''')