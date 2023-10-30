
from pprint import pprint
from MongoDB.Crud.CrudHistorico import CrudHistorico
from MongoDB.Crud.CrudProduto import CrudProduto
from MongoDB.Crud.CrudUsuario import CrudUsuario


class MenuHistorico:

    crudHistorico = CrudHistorico()
    crudUsuario = CrudUsuario()
    crudProduto = CrudProduto()


    def menu(self):
        sub = 0
        while(sub != 'V'):
            print("Menu do Histórico")
            print("1-Listar histórico de um usuário")
            print("2-Listar todos os históricos cadastrados")
            print("3-Inserir um produto em um histórico")
            sub = input("Digite a opção desejada? (V para voltar) ")
            if (sub == '1'):
                print("Listar histórico de um usuário\n")
                usuario_id = self.crudUsuario.selecionaId("exibir o histórico")
                resultado = self.crudHistorico.Find(usuario_id)
                pprint(resultado)
            elif (sub == '2'):
                print("Listar todos os históricos cadastrados\n")
                pprint(self.crudHistorico.FindAll())
            elif (sub == '3'):
                print("Inserir um produto em um histórico\n")
                usuario_id = self.crudUsuario.selecionaId("inserir o produto ao historico")
                if usuario_id == "C":
                    print("\nOperação cancelada\n")
                elif usuario_id == "Não há ninguém cadastrado":
                    print(usuario_id)
                else:
                    produto = self.crudProduto.selecionaProdutoResumido("adicionar ao histórico")
                    if produto == "C":
                        print("\nOperação cancelada\n")
                    elif produto == "Não há produtos cadastrado":
                        print(produto)
                    else:
                        self.crudHistorico.Update(usuario_id, produto)
                