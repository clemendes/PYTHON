import abc

class InterfaceVeiculo(abc.ABC):

    @abc.abstractmethod
    def detalhes(self):
        pass

    @abc.abstractmethod
    def pintar(self, cor):
        pass

    @abc.abstractmethod
    def abastecer(self, qtd_combustivel):
        pass

    @abc.abstractmethod
    def ligar(self):
        pass

    @abc.abstractmethod
    def desligar(self):
        pass

    @abc.abstractmethod
    def acelerar(self, velocidade=10):
        pass