from abc import ABC, abstractmethod
from ..Conexao import ConexaoMongoDB

class CrudAbstrato(ABC):

    
    conexao = ConexaoMongoDB()

    @abstractmethod
    def openConection(self):
        pass

    #Create
    @abstractmethod
    def Create(self, entidade):
        pass

    #Read
    @abstractmethod
    def Find(self, filtro):
        pass

    @abstractmethod
    def FindAll(self):
        pass


    #Update
    @abstractmethod
    def Update(self, id):
        pass

    #Delete
    @abstractmethod
    def Delete(self, id):
        pass