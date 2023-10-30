

class PerguntaUpdate:
    
    def pergunta(self, atributo):
        resposta = input(f"Você deseja atualizar {atributo} (sim ou nao): ")
        if resposta == "sim":
            novoAtributo = input(f"Insira o novo {atributo}: ")
            atualizacao = {"$set": {f"{atributo}":f"{novoAtributo}"}}
            return atualizacao
        else:
            return "nao"

