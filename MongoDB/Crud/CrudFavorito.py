import time
from MongoDB.Crud.CrudAbstrato import CrudAbstrato
from MongoDB.Crud.CrudProduto import CrudProduto
from MongoDB.Crud.CrudUsuario import CrudUsuario


class CrudFavorito(CrudAbstrato):

    def openConection(self):
        while True:
            try:
                self.colecao = self.conexao.get_collection("Favoritos")
                break
            except:
                print("nao foi")
                time.sleep(1)

    #Create

    def Create(self, usuario_id):
        favoritos = {
            "usuario_id":usuario_id,
            "usuario_favoritos":[]
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
            return "Não há nenhum favoritos cadastrado"


    #Update

    def Update(self, id, produto):
        self.colecao.update_one({"usuario_id":id}, {"$push":{"usuario_favoritos":produto}})
        

    #Delete - Isso já é feito pelo DeleteUsuarioCascata.py

    def Delete(self, id):
        return None