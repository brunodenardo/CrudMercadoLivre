import time
from MongoDB.Crud.CrudAbstrato import CrudAbstrato



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
        self.openConection()
        favoritos = {
            "usuario_id":usuario_id,
            "usuario_favoritos":[]
        }
        self.colecao.insert_one(favoritos)


    #Read

    def Find(self, usuario_id):
        self.openConection()
        resultado = list(self.colecao.find({"usuario_id":usuario_id}))

        if resultado == None or resultado == []:
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
        self.openConection()
        listaFavoritos = list(self.colecao.find())
        if produto not in listaFavoritos:
            self.colecao.update_one({"usuario_id":id}, {"$push":{"usuario_favoritos":produto}})
        else:
            print("\nEsse produto já está nos favoritos")
        

    #Delete - Isso já é feito pelo DeleteUsuarioCascata.py

    def Delete(self, id):
        return None