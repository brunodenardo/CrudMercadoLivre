from MongoDB.Crud.CrudProduto import CrudProduto


class DeletaRelacionados:
    crudProduto = CrudProduto()

    def deletar(self, filtro, update):
        self.crudProduto.openConection()
        self.crudProduto.colecao.update_many(filtro, update)
