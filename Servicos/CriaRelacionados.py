
from MongoDB.Crud.CrudProduto import CrudProduto


class CriaRelacionados:

    crudProduto = CrudProduto()

    def criar(self):
        resposta = input("Deseja relacionar esse produto a outro: ")
        listaRelacionados = []
        if resposta == "sim":
            while(resposta != "X"):
                self.crudProduto.openConection()
                produtoRelacionado = self.crudProduto.selecionaProdutoResumido("relacionar ao produto que está sendo criado")
                if(produtoRelacionado == "Não há produtos cadastrado"):
                    return listaRelacionados
                elif produtoRelacionado not in listaRelacionados:
                    listaRelacionados.append(produtoRelacionado)
                else:
                    print("Esse produto já está relacionado.")
                resposta = input("Quer relacionar mais algum produto a esse (sim ou nao)")
        return listaRelacionados