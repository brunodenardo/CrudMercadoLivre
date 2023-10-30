
from MongoDB.Crud.CrudCompra import CrudCompra
from MongoDB.Crud.CrudFavorito import CrudFavorito
from MongoDB.Crud.CrudHistorico import CrudHistorico
from MongoDB.Crud.CrudProduto import CrudProduto


class UpdateProdutoCascata:

    crudProduto = CrudProduto()
    crudFavorito = CrudFavorito()
    crudHistorico = CrudHistorico()
    crudCompra = CrudCompra()

    def update(self, id, atributo, alteracao):

        self.crudProduto.openConection()
        self.crudProduto.colecao.update_many({"produto_relacionado.produto_id": id}, {"$set":{"produto_relacionado":{atributo:alteracao}}})
        self.crudCompra.openConection()
        self.crudCompra.colecao.update_many({"usuario_compras.produto_id":id}, {"$set":{"usuario_compras":{atributo:alteracao}}})
        self.crudFavorito.openConection()
        self.crudFavorito.colecao.update_many({"usuario_favoritos.produto_id":id}, {"$set":{"usuario_favoritos":{atributo:alteracao}}})
        self.crudHistorico.openConection()
        self.crudHistorico.colecao.update_many({"historico_usuario.produto_id":id}, {"$set":{"historico_usuario":{atributo:alteracao}}})
        