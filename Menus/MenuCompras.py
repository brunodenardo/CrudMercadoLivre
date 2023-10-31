
from pprint import pprint
from MongoDB.Crud.CrudCompra import CrudCompra
from MongoDB.Crud.CrudUsuario import CrudUsuario
from Servicos.SelecionadorIds import SelecionadorIds


class MenuCompras:

    crudCompra = CrudCompra()
    crudUsuario = CrudUsuario()
    selecionadorIds = SelecionadorIds()


    def menu(self):
        sub = 0
        while(sub != 'V'):
            print("Menu das Compras")
            print("1-Listar compras de um usuário")
            print("2-Listar todas as compras cadastradas")
            print("3-Inserir um produto às compras de um usuário")
            sub = input("Digite a opção desejada? (V para voltar) ")
            if (sub == '1'):
                print("Listar compras de um usuário\n")
                usuario_id = self.selecionadorIds.selecionar("Usuário", "exibir as compras")
                if type(usuario_id) == str:
                    print(usuario_id)
                else:
                    resultado = self.crudCompra.Find(usuario_id)
                    pprint(resultado)
            elif (sub == '2'):
                print("Listar todas as compras cadastradas\n")
                pprint(self.crudCompra.FindAll())
            elif (sub == '3'):
                print("Inserir um produto às compras de um usuário\n")
                usuario_id = self.selecionadorIds.selecionar("Usuário", "inserir um produto nas compras desse usuário")
                if usuario_id == "C":
                    print("\nOperação cancelada\n")
                elif usuario_id == "Não há Usuário cadastrados":
                    print(usuario_id)
                else:
                    produto = self.selecionadorIds.selecionarObjeto("Produto", "adicionar as compras de um usuário")
                    if produto == "C":
                        print("\nOperação cancelada\n")
                    elif produto == "Não há produtos cadastrado":
                        print(produto)
                    else:
                        id = produto["_id"]
                        del produto["_id"]
                        produto["produto_id"] = id
                        self.crudCompra.Update(usuario_id, produto)
                