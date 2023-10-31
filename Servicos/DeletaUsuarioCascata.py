
from Servicos.DeletaRelacionados import DeletaRelacionados
from Servicos.EscolheColecao import EscolheColecao


class DeletaUsuarioCascata:

    deletaRelacionados = DeletaRelacionados()
    escolheColecao = EscolheColecao()

    def deletar(self, usuario_id):
        colecaoUsuario = self.escolheColecao.escolher("Usuário")
        colecaoProduto = self.escolheColecao.escolher("Produto")
        colecaoHistorico = self.escolheColecao.escolher("Histórico")
        colecaoFavoritos = self.escolheColecao.escolher("Favoritos")
        colecaoCompras = self.escolheColecao.escolher("Compras")
        colecaoCompras.delete_one({"usuario_id":usuario_id})
        colecaoFavoritos.delete_one({"usuario_id":usuario_id})
        colecaoHistorico.delete_one({"usuario_id":usuario_id})
        colecaoUsuario.delete_one({"_id":usuario_id})
        listaProdutos = list(colecaoProduto.find({"vendedor_id":usuario_id}))
        if listaProdutos != []:
            colecaoProduto.delete_many({"vendedor_id":usuario_id})
            for documento in listaProdutos:
                self.deletaRelacionados.deletar(
                    {"produto_relacionado.produto_id":documento["_id"]},
                    {"$pull":{"produto_relacionado": {"produto_id":documento["_id"]}}})