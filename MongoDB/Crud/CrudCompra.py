import time
from MongoDB.Crud.CrudAbstrato import CrudAbstrato


class CrudCompra(CrudAbstrato):

    
    def openConection(self):
        while True:
            try:
                self.colecao = self.conexao.get_collection("Compras")
                self.colecaoProdutos = self.conexao.get_collection("Produto")
                break
            except:
                print("nao foi")
                time.sleep(1)

    #Create

    def Create(self, usuario_id):
        self.openConection()
        favoritos = {
            "usuario_id":usuario_id,
            "usuario_compras":[]
        }
        self.colecao.insert_one(favoritos)


    #Read

    def Find(self, usuario_id):
        self.openConection()
        resultado = self.colecao.find({"usuario_id":usuario_id})

        if resultado == None:
            return "Esse usuário não existe"
        else:
            return resultado


    def FindAll(self):
        self.openConection()
        listaFavoritos = list(self.colecao.find())
        if len(listaFavoritos) != 0:
            return listaFavoritos
        else:
            return "Não há nenhum documento cadastrado em compras"


    #Update

    def Update(self, id, produto):
        self.openConection()
        self.colecao.update_one({"usuario_id":id}, {"$push":{"usuario_compras":produto}})
        produto = self.colecaoProdutos.find_one({"_id":produto["produto_id"]})
        self.colecaoProdutos.update_one({"_id":produto["_id"]}, {"$set":{"produto_numero_vendas":(produto["produto_numero_vendas"] + 1)}})
        

    #Delete - Isso já é feito pelo DeleteUsuarioCascata.py

    def Delete(self, id):
        return None