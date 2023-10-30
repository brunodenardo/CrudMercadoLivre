from MongoDB.Crud.CrudCompra import CrudCompra
from MongoDB.Crud.CrudFavorito import CrudFavorito
from MongoDB.Crud.CrudHistorico import CrudHistorico
from MongoDB.Crud.CrudProduto import CrudProduto


class DeleteProdutoCascata:
    

    crudProduto = CrudProduto()
    crudFavorito = CrudFavorito()
    crudHistorico = CrudHistorico()
    crudCompra = CrudCompra()

    def deletar(self, id):

        self.crudProduto.openConection()
        self.deletaRelacionados.deletar({"produto_relacionado.produto_id":id}, {"$pull":{"produto_relacionado": {"produto_id":id}}})
        self.crudCompra.openConection()
        self.crudCompra.colecao.update_many({"usuario_compras.produto_id":id}, {"$pull":{"usuario_compras":{"produto_id":id}}})
        self.crudFavorito.openConection()
        self.crudFavorito.colecao.update_many({"usuario_favoritos.produto_id":id}, {"$pull":{"usuario_favoritos":{"produto_id":id}}})
        self.crudHistorico.openConection()
        self.crudHistorico.colecao.update_many({"historico_usuario.produto_id":id}, {"$pull":{"historico_usuario":{"produto_id":id}}})