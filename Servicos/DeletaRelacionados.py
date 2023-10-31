from Servicos.EscolheColecao import EscolheColecao


class DeletaRelacionados:
    

    def deletar(self, filtro, update):
        escolheColecao = EscolheColecao()
        colecaoProduto = escolheColecao.escolher("Produto")
        colecaoProduto.update_many(filtro, update)
