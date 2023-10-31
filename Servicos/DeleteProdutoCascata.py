
from Servicos.EscolheColecao import EscolheColecao


class DeleteProdutoCascata:
    

    escolherColecao = EscolheColecao()

    def deletar(self, id):
        colecaoProduto = self.escolherColecao.escolher("Produto")
        colecaoProduto.update_many({"produto_relacionado.produto_id":id}, {"$pull":{"produto_relacionado": {"produto_id":id}}})
        colecaoCompra = self.escolherColecao.escolher("Compras")
        colecaoCompra.update_many({"usuario_compras.produto_id":id}, {"$pull":{"usuario_compras":{"produto_id":id}}})
        colecaoFavorito = self.escolherColecao.escolher("Favoritos")
        colecaoFavorito.update_many({"usuario_favoritos.produto_id":id}, {"$pull":{"usuario_favoritos":{"produto_id":id}}})
        colecaoHistorico = self.escolherColecao.escolher("Histórico")
        colecaoHistorico.update_many({"historico_usuario.produto_id":id}, {"$pull":{"historico_usuario":{"produto_id":id}}})