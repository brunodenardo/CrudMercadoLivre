
from pprint import pprint
from MongoDB.Crud.CrudProduto import CrudProduto
from MongoDB.Crud.CrudUsuario import CrudUsuario
from Servicos.SelecionadorIds import SelecionadorIds


class MenuProdutos:

    crudProduto = CrudProduto()
    selecionadorIds = SelecionadorIds()

    def menu(self):
        sub = 0
        while(sub != 'V'):
            print("Menu do Produto")
            print("1-Create Produto")
            print("2-Read Produto")
            print("3-Read todos os Produtos")
            print("4-Update Produto")
            print("5-Delete Produto")
            print("6-Inserir um comentário em um produto")
        
            sub = input("Digite a opção desejada? (V para voltar) ")
            if (sub == '1'):
                print("Create produto")
                self.crudProduto.Create()
            elif (sub == '2'):
                resultado = self.crudProduto.Find(self.selecionadorIds.selecionar("Produto", "listar"))
                pprint(resultado)
            elif (sub == '3'):
                print("Lista de todos os produtos:")
                resultado = self.crudProduto.FindAll()
                pprint(resultado)
            elif (sub == '4'):
                id = self.crudProduto.selecionaId("alterar")
                if id == "C":
                    print("Operação cancelada")
                elif id != "Não há produtos cadastrado":
                    self.crudProduto.Update(id)
                else:
                    print(id)
            elif (sub == '5'):
                print("delete produto")
                id = self.selecionadorIds.selecionar("Produto", "deletar")
                if id == "C":
                    print("Operação cancelada")
                elif id != "Não há Produto cadastrados":
                    self.crudProduto.Delete(id)
                else:
                    print(id)
            elif (sub == '6'):
                print("Inserir um comentário")
                comentador = self.selecionadorIds.selecionarObjeto("Usuário", "que comente")
                produto_id = self.selecionadorIds.selecionar("Produto", "que seja comentado")
                if(produto_id == "C"):
                    print("Operação cancelada")
                elif(produto_id == "Não há Produto cadastrados"):
                    print("Não há Produtos cadastrados")
                else:
                    self.crudProduto.inserirComentario(comentador, produto_id)
                
            