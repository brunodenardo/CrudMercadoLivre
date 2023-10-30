
from Menus.MenuUsuario import MenuUsuario


class MenuPrincipal:

    menuUsuario = MenuUsuario()


    def menu(self):
        key = 0
        sub = 0
        while (key != 'S'):
            print("1-CRUD Usuário")
            print("2-CRUD Historico")
            print("3-CRUD Produto")
            print("4-CRUD Favoritos")
            print("5-CRUD Compras")
            key = input("Digite a opção desejada? (S para sair) ")

            if (key == '1'):
                self.menuUsuario.menu()

            elif (key == '2'):
                print("Menu do Vendedor")        
            elif (key == '3'):
                print("Menu do Produto")        

        print("Tchau")
