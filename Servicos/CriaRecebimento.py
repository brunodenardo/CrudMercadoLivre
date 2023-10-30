class CriaRecebimento:

    def criar(self):
        resposta = "sim"
        recebimentos = []
        while (resposta == "sim"):
            recebimento = self.criarRecebimento()
            recebimentos.append(recebimento)
            resposta = input("Deseja cadastrar outro endereço (sim ou nao): ")
        return recebimentos


    def criarRecebimento(self):
        recebimento = {}
        atributos = ['recebimento_agencia', 'recebimento_banco', 'recebimento_conta']
        for atributo in atributos:
            valor = input(f"Digite o valor de {atributo}: ")
            recebimento[atributo] = valor
        return recebimento