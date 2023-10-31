
from MongoDB.Crud.CrudCompra import CrudCompra
from MongoDB.Crud.CrudFavorito import CrudFavorito
from MongoDB.Crud.CrudHistorico import CrudHistorico
from Servicos.EscolheColecao import EscolheColecao



class UpdateProdutoCascata:

    escolherColecao = EscolheColecao()

    def update(self, id, atributo, alteracao):

        colecaoProduto = self.escolherColecao.escolher("Produto")
        colecaoProduto.update_many({"produto_relacionado.produto_id": id}, {"$set":{"produto_relacionado":{atributo:alteracao}}})
        colecaoCompras = self.escolherColecao.escolher("Compras")
        colecaoCompras.update_many({"usuario_compras.produto_id":id}, {"$set":{"usuario_compras":{atributo:alteracao}}})
        colecaoFavoritos = self.escolherColecao.escolher("Favoritos")
        colecaoFavoritos.update_many({"usuario_favoritos.produto_id":id}, {"$set":{"usuario_favoritos":{atributo:alteracao}}})
        colecaoHistorico = self.escolherColecao.escolher("Histórico")
        colecaoHistorico.update_many({"historico_usuario.produto_id":id}, {"$set":{"historico_usuario":{atributo:alteracao}}})
        