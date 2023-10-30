
from Servicos.CriaEndereco import CriaEndereco
from Servicos.CriaPagamento import CriaPagamento
from Servicos.CriaRecebimento import CriaRecebimento


class CriaUsuario:
        
        criaEndereco = CriaEndereco()
        criaPagamento = CriaPagamento()
        criaRecebimento = CriaRecebimento()

        
        def criar(self):
            usuario = {}
            atributos = ['usuario_email', 'usuario_endereco', 'usuario_login', 'usuario_nome', 'usuario_pagamento', 'usuario_recebimento', 'usuario_senha', 'usuario_telefone']
            for atributo in atributos:
                if(atributo != "usuario_endereco" and atributo != "usuario_pagamento" and atributo != "usuario_recebimento"):
                    valor = input(f"Digite o valor de {atributo}: ")
                    usuario[atributo] = valor      
                elif atributo == "usuario_endereco":
                    usuario["usuario_endereco"] = self.criaEndereco.criar()
                elif atributo == "usuario_pagamento":
                    usuario["usuario_pagamento"] = self.criaPagamento.criar()
                elif atributo == "usuario_recebimento":
                    usuario["usuario_recebimento"] = self.criaRecebimento.criar()
            return usuario
                    