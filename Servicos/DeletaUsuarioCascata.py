from MongoDB.Crud.CrudProduto import CrudProduto
from MongoDB.Crud.CrudUsuario import CrudUsuario
from Servicos.DeletaRelacionados import DeletaRelacionados


class DeletaUsuarioCascata:
    crudUsuario = CrudUsuario()
    crudProduto = CrudProduto()
    deletaRelacionados = DeletaRelacionados()

    def deletar(self, usuario_id):
        self.crudUsuario.openConection()
        self.crudUsuario.colecao.delete_one({"_id":usuario_id})
        listaProdutos = list(self.crudProduto.colecao.find({"vendedor_id":usuario_id}))
        if listaProdutos != []:
            self.crudProduto.colecao.delete_many({"vendedor_id":usuario_id})
            for documento in listaProdutos:
                self.deletaRelacionados.deletar(
                    {"produto_relacionado.produto_id":documento["_id"]},
                    {"$pull":{"produto_relacionado": {"produto_id":documento["_id"]}}})