

from pprint import pprint
from MongoDB.Crud.CrudUsuario import CrudUsuario
from Servicos.SelecionadorIds import SelecionadorIds


class MenuUsuario:

    crudUsuario = CrudUsuario()
    selecionadorIds = SelecionadorIds()

    def menu(self):
        sub = 0
        while(sub != 'V'):
            print("Menu do Usuário")
            print("1-Create Usuário")
            print("2-Read Usuário")
            print("3-Read todos os Usuários")
            print("4-Update Usuário")
            print("5-Delete Usuário")
            sub = input("Digite a opção desejada? (V para voltar) ")
            if (sub == '1'):
                print("Create usuario")
                self.crudUsuario.Create()
            elif (sub == '2'):
                resultado = self.crudUsuario.Find(self.selecionadorIds.selecionar("Usuário", "listar"))
                pprint(resultado)
            elif (sub == '3'):
                print("Lista de todos os usuários:")
                resultado = self.crudUsuario.FindAll()
                pprint(resultado)
            elif (sub == '4'):
                id = self.selecionadorIds.selecionar("Usuário", "alterar")
                if id != "Não há Usuário cadastrados":
                    self.crudUsuario.Update(id)
                else:
                    print(id)
            elif (sub == '5'):
                print("delete usuario")
                id = self.selecionadorIds.selecionar("Usuário", "deletar")
                if id != "Não há Usuário cadastrados":
                    self.crudUsuario.Delete(id)
                else:
                    print(id)
                
            