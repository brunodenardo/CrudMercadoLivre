

from pprint import pprint
from Servicos.EscolheColecao import EscolheColecao
from Servicos.PerguntaUpdate import PerguntaUpdate


class UpdateAninhado:

    perguntaUpdate = PerguntaUpdate()
    escolheColecao = EscolheColecao()

    def update(self, documento, atributoPai, filtro, colecaoAlvo):
        elemento = 0
        for aninhado in documento[atributoPai]:
            for chave, valor in aninhado.items():
                print(f"\nVocê está em {atributoPai} {elemento}")
                print(f"Atributo: {chave} \nValor Atual: {valor}")
                atributoAninhado = f"{atributoPai}.{elemento}.{chave}"
                update = self.perguntaUpdate.pergunta(atributoAninhado)
                if update != 'nao':
                    colecao = self.escolheColecao.escolher(colecaoAlvo)
                    colecao.update_one(filtro, update)
            elemento += 1
        

