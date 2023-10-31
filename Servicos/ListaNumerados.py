class ListaNumerados:


    def listaProdutos(self, listaTodos):
        listaResultado = []
        if len(listaTodos) == 0:
            return f"Não há produtos cadastrados"
        else:
            contagem = 0
            for documento in listaTodos:
                objeto ={
                    "numero":contagem,
                    "_id":documento["_id"],
                    "produto_nome":documento["produto_nome"],
                    "produto_preco": documento["produto_preco"],
                    "produto_oferta":documento["produto_oferta"]
                }
                contagem += 1
                listaResultado.append(objeto)
            return listaResultado

    def listaUsuarios(self, listaTodos):
        listaResultado = []
        if len(listaTodos) == 0:
            return "Não há ninguém cadastrado"
        else:
            contagem = 0
            for documento in listaTodos:
                objeto ={
                    "numero":contagem,
                    "_id":documento["_id"],
                    "usuario_nome":documento["usuario_nome"]
                }
                contagem += 1
                listaResultado.append(objeto)
            return listaResultado

    def escolheListagem(self, listaTodos, colecao):
        if colecao == "Produto":
            return self.listaProdutos(listaTodos)
        elif colecao == "Usuário":
            return self.listaUsuarios(listaTodos)