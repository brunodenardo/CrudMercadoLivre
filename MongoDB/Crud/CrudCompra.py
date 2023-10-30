import time
from MongoDB.Crud.CrudAbstrato import CrudAbstrato


class CrudCompra(CrudAbstrato):
    
    def openConection(self):
        while True:
            try:
                self.colecao = self.conexao.get_collection("Compras")
                break
            except:
                print("nao foi")
                time.sleep(1)

    #Create

    def Create(self, usuario_id):
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
        self.colecao.update_one({"usuario_id":id}, {"$push":{"usuario_compras":produto}})
        

    #Delete - Isso já é feito pelo DeleteUsuarioCascata.py

    def Delete(self, id):
        return None