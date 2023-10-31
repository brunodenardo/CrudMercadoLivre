
from pprint import pprint
from MongoDB.Crud.CrudFavorito import CrudFavorito
from Servicos.SelecionadorIds import SelecionadorIds


class MenuFavoritos:

    crudFavorito = CrudFavorito()
    selecionadorIds = SelecionadorIds()


    def menu(self):
        sub = 0
        while(sub != 'V'):
            print("Menu dos Favoritos")
            print("1-Listar os favoritos de um usuário")
            print("2-Listar todos os favoritos cadastradas")
            print("3-Inserir um produto aos favoritos de um usuário")
            sub = input("Digite a opção desejada? (V para voltar) ")
            if (sub == '1'):
                print("Listar os favoritos de um usuário\n")
                usuario_id = self.selecionadorIds.selecionar("Usuário", "exibir os favoritos")
                resultado = self.crudFavorito.Find(usuario_id)
                pprint(resultado)
            elif (sub == '2'):
                print("Listar todos os favoritos cadastradas\n")
                pprint(self.crudFavorito.FindAll())
            elif (sub == '3'):
                print("Inserir um produto aos favoritos de um usuário\n")
                usuario_id = self.selecionadorIds.selecionar("Usuário", "inserir um produto nos favoritos desse usuário")
                if usuario_id == "C":
                    print("\nOperação cancelada\n")
                elif usuario_id == "Não há ninguém cadastrado":
                    print(usuario_id)
                else:
                    produto = self.selecionadorIds.selecionarObjeto("Produto", "adicionar aos favoritos de um usuário")
                    if produto == "C":
                        print("\nOperação cancelada\n")
                    elif produto == "Não há produtos cadastrado":
                        print(produto)
                    else:
                        id = produto["_id"]
                        del produto["_id"]
                        produto["produto_id"]
                        self.crudFavorito.Update(usuario_id, produto)
                