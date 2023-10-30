from pprint import pprint
import time
from MongoDB.Crud.CrudAbstrato import CrudAbstrato
from Servicos.CriaProduto import CriaProduto
from Servicos.DeletaRelacionados import DeletaRelacionados
from Servicos.DeleteProdutoCascata import DeleteProdutoCascata
from Servicos.PerguntaUpdate import PerguntaUpdate
from Servicos.UpdateAninhado import UpdateAninhado
from Servicos.UpdateProdutoCascata import UpdateProdutoCascata


class CrudProduto(CrudAbstrato):

    perguntaUpdate = PerguntaUpdate()
    updateAninhado = UpdateAninhado()
    criarProduto = CriaProduto()
    deletaRelacionados = DeletaRelacionados()
    deleteProdutoCascata = DeleteProdutoCascata()
    updateProdutoCascata = UpdateProdutoCascata()

    def openConection(self):
        while True:
            try:
                self.colecao = self.conexao.get_collection("Produto")
                break
            except:
                print("nao foi")
                time.sleep(1)


    #Create
    def Create(self):
        produto = self.criarProduto.criar()
        if(type(produto) != str):
            self.openConection()
            self.colecao.insert_one(produto)
        else:
            print(produto)

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
            return "Não há produtos cadastrados"
        else:
            contagem = 0
            for documento in resultado:
                objeto ={
                    "numero":contagem,
                    "_id":documento["_id"],
                    "produto_nome":documento["produto_nome"],
                    "produto_preco": documento["produto_preco"],
                    "produto_oferta":documento["produto_oferta"]
                }
                contagem += 1
                listaResultado.append(objeto)
            return listaResultado

    def selecionaId(self, acao):
        self.openConection()
        listaProduto = self.FindAll()
        numero = ""
        if type(listaProduto) != str:
            while numero != "C":
                pprint(listaProduto)
                numero = input(f"Selecione o número do produto que você quer {acao} (C para cancelar): ")
                if numero.isdigit() and int(numero) < len(listaProduto):
                    return listaProduto[int(numero)]["_id"]
                else:
                    print("Esse número não corresponde a nenhum produto.\n")
            return "C"
        else:
            return "Não há produtos cadastrado"

    def selecionaProdutoResumido(self, acao):
        self.openConection()
        listaProduto = self.FindAll()
        numero = ""
        if type(listaProduto) != str:
            while numero != "C":
                pprint(listaProduto)
                numero = input(f"Selecione o número do produto que você quer {acao} (C para cancelar): ")
                if numero.isdigit() and int(numero) < len(listaProduto):
                    produtoEscolhido = listaProduto[int(numero)]
                    del produtoEscolhido["numero"]
                    return listaProduto[int(numero)]
                else:
                    print("Esse número não corresponde a nenhum produto.\n")
            return "C"
        else:
            return "Não há produtos cadastrado"

    #Update
    def Update(self, id):
        self.openConection()
        documento = self.Find()
        id=documento["_id"]
        if type(documento) != str:
            atributos = ["produto_nome", "produto_descricao", "produto_preco", "produto_oferta"]
            for atributo in atributos:
                update = self.perguntaUpdate.pergunta(atributo)
                if update != "nao":
                    self.colecao.update_one({"_id":id}, update)
                    self.updateProdutoCascata.update(id, atributo, update["$set"][atributo])

    def inserirComentario(self, comentador, produto_id):
        comentario = input("Digite seu comentário")
        objetoComentario = {
            "usuario_id":comentador["_id"],
            "usuario_nome":comentador["usuario_nome"],
            "comentario":comentario
        }
        self.openConection()
        self.colecao.update_one({"_id":produto_id}, {"$push":{"produto_comentarios":objetoComentario}})


    #Delete
    def Delete(self, id):
        filtro = {"_id":id}
        self.colecao.delete_one(filtro)
        self.deleteProdutoCascata.deletar(id)

        