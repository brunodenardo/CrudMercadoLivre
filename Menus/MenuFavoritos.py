import pprint
from MongoDB.Crud.CrudFavorito import CrudFavorito
from MongoDB.Crud.CrudProduto import CrudProduto
from MongoDB.Crud.CrudUsuario import CrudUsuario


class MenuFavoritos:

    crudFavorito = CrudFavorito()
    crudUsuario = CrudUsuario()
    crudProduto = CrudProduto()


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
                usuario_id = self.crudUsuario.selecionaId("exibir os favoritos")
                resultado = self.crudFavorito.Find(usuario_id)
                pprint(resultado)
            elif (sub == '2'):
                print("Listar todos os favoritos cadastradas\n")
                pprint(self.crudFavorito.FindAll())
            elif (sub == '3'):
                print("Inserir um produto aos favoritos de um usuário\n")
                usuario_id = self.crudUsuario.selecionaId("inserir um produto nos favoritos desse usuário")
                if usuario_id == "C":
                    print("\nOperação cancelada\n")
                elif usuario_id == "Não há ninguém cadastrado":
                    print(usuario_id)
                else:
                    produto = self.crudProduto.selecionaProdutoResumido("adicionar aos favoritos de um usuário")
                    if produto == "C":
                        print("\nOperação cancelada\n")
                    elif produto == "Não há produtos cadastrado":
                        print(produto)
                    else:
                        self.crudFavorito.Update(usuario_id, produto)
                