import time
from MongoDB.Crud.CrudAbstrato import CrudAbstrato
from pprint import pprint
from MongoDB.Crud.CrudCompra import CrudCompra
from MongoDB.Crud.CrudFavorito import CrudFavorito
from MongoDB.Crud.CrudHistorico import CrudHistorico
from Servicos.CriaUsuario import CriaUsuario
from Servicos.DeletaUsuarioCascata import DeletaUsuarioCascata

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

    def openConection(self):
        while True:
            try:
                self.colecao = self.conexao.get_collection("Usuário")
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
        listaResultado = []
        if len(resultado) == 0:
            return "Não há ninguém cadastrado"
        else:
            contagem = 0
            for documento in resultado:
                objeto ={
                    "numero":contagem,
                    "_id":documento["_id"],
                    "usuario_nome":documento["usuario_nome"]
                }
                contagem += 1
                listaResultado.append(objeto)
            return listaResultado
        
    def selecionaId(self, acao):
        self.openConection()
        listaUsuario = self.FindAll()
        numero = ""
        if type(listaUsuario) != str:
            while numero != "C":
                pprint(listaUsuario)
                numero = input(f"Selecione o número do usuário que você quer {acao} (C para cancelar): ")
                if numero.isdigit() and int(numero) < len(listaUsuario):
                    return listaUsuario[int(numero)]["_id"]
                else:
                    print("Esse número não corresponde a nenhum usuário.\n")
            return "C"
        else:
            return "Não há ninguém cadastrado"
            
        

    #Update

    def Update(self, id):
        self.openConection()
        documento = self.Find(id)
        id=documento["_id"]
        if type(documento) != str:
            atributos = ['usuario_email', 'usuario_endereco', 'usuario_login', 'usuario_nome', 'usuario_pagamento', 'usuario_recebimento', 'usuario_senha', 'usuario_telefone']
            for atributo in atributos:
                if atributo != 'usuario_endereco' and atributo != 'usuario_pagamento' and atributo != 'usuario_recebimento':
                    update = self.perguntaUpdate.pergunta(atributo)
                    if update != 'nao':
                        self.colecao.update_one({"_id":id}, update)
                elif atributo == 'usuario_endereco':
                    self.updateAninhado.update(documento, atributo, {"_id":id}, "Usuário")
                elif atributo == 'usuario_recebimento':
                    self.updateAninhado.update(documento, atributo, {"_id":id}, "Usuário")
                elif atributo == 'usuario_pagamento':  
                    self.updateAninhado.update(documento, atributo, {"_id":id}, "Usuário")
        else:
            print(documento)


    def UpdateCascata(self, id, filtro, alteracao):
        return None

    #Delete

    def Delete(self, id):
        self.deletaUsuariosCascata.deletar(id)
        
        