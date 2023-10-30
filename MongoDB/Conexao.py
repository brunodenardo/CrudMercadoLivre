
from pymongo import MongoClient
from pymongo.server_api import ServerApi


class ConexaoMongoDB:
    
    def __init__(self):
        connection_uri="mongodb+srv://brunodenardo:Goiabada2@clusterteste.mwsgsfj.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(connection_uri, server_api=ServerApi('1'))
        self.db = self.client["MercadoLivre"]


    def get_collection(self, colecao):
        return self.db[colecao]

    def close_connection(self):
        self.client.close()