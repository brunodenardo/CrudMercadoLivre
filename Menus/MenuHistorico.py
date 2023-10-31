
from pprint import pprint
from MongoDB.Crud.CrudHistorico import CrudHistorico
from Servicos.SelecionadorIds import SelecionadorIds


class MenuHistorico:

    crudHistorico = CrudHistorico()
    selecionadorId = SelecionadorIds()

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
                usuario_id = self.selecionadorId.selecionar("Usuário", "exibir o histórico")
                resultado = self.crudHistorico.Find(usuario_id)
                pprint(resultado)
            elif (sub == '2'):
                print("Listar todos os históricos cadastrados\n")
                pprint(self.crudHistorico.FindAll())
            elif (sub == '3'):
                print("Inserir um produto em um histórico\n")
                usuario_id = self.selecionadorId.selecionar("Usuário","inserir o produto ao historico")
                if usuario_id == "C":
                    print("\nOperação cancelada\n")
                elif usuario_id == "Não há ninguém cadastrado":
                    print(usuario_id)
                else:
                    produto = self.selecionadorId.selecionarObjeto("Produto", "adicionar ao histórico")
                    if produto == "C":
                        print("\nOperação cancelada\n")
                    elif produto == "Não há produtos cadastrado":
                        print(produto)
                    else:
                        id = produto["_id"]
                        del produto["_id"]
                        produto["produto_id"] = id
                        self.crudHistorico.Update(usuario_id, produto)
                