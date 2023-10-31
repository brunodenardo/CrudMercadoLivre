


from Servicos.SelecionadorIds import SelecionadorIds


class CriaRelacionados:

    selecionadorIds = SelecionadorIds()

    def criar(self):
        resposta = input("Deseja relacionar esse produto a outro (sim ou nao): ")
        listaRelacionados = []
        if resposta == "sim":
            while(resposta != "nao"):
                produtoRelacionado = self.selecionadorIds.selecionarObjeto("Produto", "relacionar ao produto que está sendo criado")
                if(produtoRelacionado == "Não há produtos cadastrado"):
                    return listaRelacionados
                elif produtoRelacionado not in listaRelacionados:
                    listaRelacionados.append(produtoRelacionado)
                else:
                    print("Esse produto já está relacionado.")
                resposta = input("Quer relacionar mais algum produto a esse (sim ou nao)")
        return listaRelacionados