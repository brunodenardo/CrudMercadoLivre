


from MongoDB.Conexao import ConexaoMongoDB


class EscolheColecao:

    conexao = ConexaoMongoDB()

    def escolher(self, colecao):
        if colecao == "Usuário":
            colecao = self.conexao.get_collection("Usuário")
        elif colecao == "Produto":
            colecao = self.conexao.get_collection("Produto")
        elif colecao == "Favoritos":
            colecao = self.conexao.get_collection("Favoritos")
        elif colecao == "Histórico":
            colecao = self.conexao.get_collection("Histórico")
        elif colecao == "Compras":
            colecao = self.conexao.get_collection("Compras")
        else:
            return "Colecao não existente"
        return colecao