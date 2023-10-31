


from Servicos.CriaRelacionados import CriaRelacionados
from Servicos.SelecionadorIds import SelecionadorIds


class CriaProduto:

    criaRelacionado = CriaRelacionados()
    selecionadorIds = SelecionadorIds()

    def criar(self):
        produto = {}
        atributos = ["produto_nome", "produto_descricao", "produto_preco", "produto_oferta", "produto_numero_vendas", "vendedor_id", "produto_comentarios", "produto_relacionado"]
        for atributo in atributos:
            if(atributo != "vendedor_id" and atributo != "produto_comentarios" and atributo != "produto_relacionado" and atributo != "produto_numero_vendas"):
                valor = input(f"Digite o valor de {atributo}: ")
                produto[atributo] = valor
            elif(atributo == "vendedor_id"):
                
                id = self.selecionadorIds.selecionar("Usuário", "atrelar a esse produto como vendedor")
                if(id != "Não há Usuário cadastrados"):
                    produto[atributo] = id
                else:
                    return "Não é possível cadastrar um produto sem que haja um usuário cadastrado"
            elif(atributo == "produto_comentarios"):
                produto[atributo] = []
            elif(atributo == "produto_relacionado"):
                relacionados = self.criaRelacionado.criar()
                if type(relacionados):
                    print(relacionados)
                else:
                    produto[atributo] = relacionados
            elif(atributo == "produto_numero_vendas"):
                produto[atributo] = 0
        return produto
