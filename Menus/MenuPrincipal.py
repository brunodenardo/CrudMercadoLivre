
from Menus.MenuCompras import MenuCompras
from Menus.MenuFavoritos import MenuFavoritos
from Menus.MenuHistorico import MenuHistorico
from Menus.MenuProdutos import MenuProdutos
from Menus.MenuUsuario import MenuUsuario


class MenuPrincipal:

    menuUsuario = MenuUsuario()
    menuHistorico = MenuHistorico()
    menuCompras = MenuCompras()
    menuFavoritos = MenuFavoritos()
    menuProduto = MenuProdutos()


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
                self.menuHistorico.menu()
            elif (key == '3'):
                self.menuProduto.menu()
            elif (key == '4'):
                self.menuFavoritos.menu()
            elif (key == '5'):
                self.menuCompras.menu()      

        print("Tchau")
