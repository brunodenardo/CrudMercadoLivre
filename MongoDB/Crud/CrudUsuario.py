import time
from MongoDB.Crud.CrudAbstrato import CrudAbstrato
from pprint import pprint
from MongoDB.Crud.CrudCompra import CrudCompra
from MongoDB.Crud.CrudFavorito import CrudFavorito
from MongoDB.Crud.CrudHistorico import CrudHistorico
from Servicos.CriaUsuario import CriaUsuario
from Servicos.DeletaUsuarioCascata import DeletaUsuarioCascata
from Servicos.ListaNumerados import ListaNumerados

from Servicos.PerguntaUpdate import PerguntaUpdate
from Servicos.UpdateAninhado import UpdateAninhado

class CrudUsuario(CrudAbstrato):
    
    perguntaUpdate = PerguntaUpdate()
    criaUsuario = CriaUsuario()
    updateAninhado = UpdateAninhado()
    deletaUsuariosCascata = DeletaUsuarioCascata()
    crudHistorico = CrudHistorico()
    crudCompra = CrudCompra()
    crudFavorito = CrudFavorito()
    listaNumerados = ListaNumerados()

    def openConection(self):
        while True:
            try:
                self.colecao = self.conexao.get_collection("Usuário")
                self.colecaoProduto = self.conexao.get_collection("Produto")
                break
            except:
                print("nao foi")
                time.sleep(1)


    #Create
    def Create(self):
        usuario = self.criaUsuario.criar()
        self.openConection()
        resultado =self.colecao.insert_one(usuario)
        self.crudFavorito.Create(resultado.inserted_id)
        self.crudCompra.Create(resultado.inserted_id)
        self.crudHistorico.Create(resultado.inserted_id)


    #Read

    def Find(self, id):
        self.openConection()
        filtro = {"_id":id}
        resultado = self.colecao.find_one(filtro)

        if resultado == None:
            return "Não há ninguém cadastrado"
        else:
            return resultado
        

    def FindAll(self):
        self.openConection()
        resultado = list(self.colecao.find())
        return resultado
        
            
        

    #Update

    def Update(self, id):
        self.openConection()
        documento = self.Find(id)
        id=documento["_id"]
        if type(documento) != str:
            atributos = ['usuario_email', 'usuario_endereco', 'usuario_login', 'usuario_nome', 'usuario_pagamento', 'usuario_recebimento', 'usuario_senha', 'usuario_telefone']
            for atributo in atributos:
                if atributo != 'usuario_endereco' and atributo != 'usuario_pagamento' and atributo != 'usuario_recebimento' and atributo != "usuario_nome":
                    update = self.perguntaUpdate.pergunta(atributo)
                    if update != 'nao':
                        self.colecao.update_one({"_id":id}, update)
                elif atributo == 'usuario_endereco':
                    self.updateAninhado.update(documento, atributo, {"_id":id}, "Usuário")
                elif atributo == 'usuario_recebimento':
                    self.updateAninhado.update(documento, atributo, {"_id":id}, "Usuário")
                elif atributo == 'usuario_pagamento':  
                    self.updateAninhado.update(documento, atributo, {"_id":id}, "Usuário")
                elif atributo == 'usuario_nome':
                    update = self.perguntaUpdate.pergunta(atributo)
                    if update != 'nao':
                        self.colecao.update_one({"_id":id}, update)
                        print(f"ATRIBUTO:  {update['$set'][atributo]}")
                        self.colecaoProduto.update_many({"produto_comentarios.usuario_id":id}, {"$set":{"produto_comentarios.$[elemento].usuario_nome":update["$set"][atributo]}},array_filters=[{"elemento.usuario_id": id}])
        else:
            print(documento)




    #Delete

    def Delete(self, id):
        self.deletaUsuariosCascata.deletar(id)
        
        