

class CriaEndereco:

    def criar(self):
        resposta = "sim"
        enderecos = []
        while (resposta == "sim"):
            endereco = self.criarEndereco()
            enderecos.append(endereco)
            resposta = input("Deseja cadastrar outro endereço (sim ou nao): ")
        return enderecos


    def criarEndereco(self):
        endereco = {}
        atributos = ['endereco_bairro', 'endereco_cep', 'endereco_estado', 'endereco_numero', 'endereco_rua_avenida','endereco_tipo', 'endereco_informacao_adicional']
        for atributo in atributos:
            valor = input(f"Digite o valor de {atributo}: ")
            endereco[atributo] = valor
        return endereco