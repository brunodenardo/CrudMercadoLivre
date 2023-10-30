import datetime
import time
from MongoDB.Crud.CrudAbstrato import CrudAbstrato
from MongoDB.Crud.CrudProduto import CrudProduto
from MongoDB.Crud.CrudUsuario import CrudUsuario


class CrudHistorico(CrudAbstrato):

    crudUsuario = CrudUsuario()
    crudProduto = CrudProduto()

    def openConection(self):
        while True:
            try:
                self.colecao = self.conexao.get_collection("Histórico")
                break
            except:
                print("nao foi")
                time.sleep(1)

    #Create

    def Create(self, usuario_id):
        historico = {
            "usuario_id":usuario_id,
            "historico_usuario":[]
        }
        self.colecao.insert_one(historico)


    #Read

    def Find(self, usuario_id):
        self.openConection()
        resultado = self.colecao.find({"usuario_id":usuario_id})

        if resultado == None:
            return "Não há ninguém cadastrado"
        else:
            return resultado


    def FindAll(self):
        self.openConection()
        listaHistoricos = list(self.colecao.find())
        if len(listaHistoricos) != 0:
            return listaHistoricos
        else:
            return "Não há nenhum histórico cadastrado"


    #Update

    def Update(self, id, produto):
        produto["produto_data_visualizacao"] = datetime.datetime.now()
        self.colecao.update_one({"usuario_id":id}, {"$push":{"historico_usuario":produto}})


    #Delete - Isso já é feito pelo DeleteUsuarioCascata.py

    def Delete(self, id):
        return None