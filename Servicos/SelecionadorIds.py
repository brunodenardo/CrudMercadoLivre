
from pprint import pprint
from Servicos.EscolheColecao import EscolheColecao
from Servicos.ListaNumerados import ListaNumerados


class SelecionadorIds:

    escolheColecao = EscolheColecao()
    listaNumerados = ListaNumerados()

    def selecionar(self, colecaoNome, acao):
        colecao = self.escolheColecao.escolher(colecaoNome)
        lista = list(colecao.find())
        lista = self.listaNumerados.escolheListagem(lista, colecaoNome)
        numero = ""
        if type(lista) != str:
            while numero != "C":
                pprint(lista)
                numero = input(f"Selecione o número do {colecaoNome} que você quer {acao} (C para cancelar): ")
                if numero.isdigit() and int(numero) < len(lista):
                    return lista[int(numero)]["_id"]
                else:
                    print(f"Esse número não corresponde a nenhum {colecaoNome}.\n")
            return "C"
        else:
            return f"Não há {colecaoNome} cadastrados"

    def selecionarObjeto(self, colecaoNome, acao):
        colecao = self.escolheColecao.escolher(colecaoNome)
        lista = list(colecao.find())
        lista = self.listaNumerados.escolheListagem(lista, colecaoNome)
        numero = ""
        if type(lista) != str:
            while numero != "C":
                pprint(lista)
                numero = input(f"Selecione o número do {colecaoNome} que você quer {acao} (C para cancelar): ")
                if numero.isdigit() and int(numero) < len(lista):
                    return lista[int(numero)]
                else:
                    print(f"Esse número não corresponde a nenhum {colecaoNome}.\n")
            return "C"
        else:
            return f"Não há {colecaoNome} cadastrado"