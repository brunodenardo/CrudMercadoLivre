class CriaPagamento:

    def criar(self):
        resposta = "sim"
        pagamentos = []
        while (resposta == "sim"):
            pagamento = self.criarPagamento()
            pagamentos.append(pagamento)
            resposta = input("Deseja cadastrar outra forma de pagamento (sim ou nao): ")
        return pagamentos


    def criarPagamento(self):
        pagamento = {}
        atributos = ['pagamento_tipo', 'pagamento_cartao']
        for atributo in atributos:
            valor = input(f"Digite o valor de {atributo}: ")
            pagamento[atributo] = valor
        return pagamento