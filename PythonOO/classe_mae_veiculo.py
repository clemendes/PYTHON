import abc, interface_veiculo

class Veiculo(interface_veiculo.InterfaceVeiculo, abc.ABC):
    # Adicionando DOCSTRING
    """Essa é a classe carro. Esta classe é utilizada para instanciar novos carros em nosso programa."""

    # Método Constructor = Inicializa
    # def = Define Funções
    def __init__(self, cor, tipo_combustivel, potencia):
        self._cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0.00
        self.__is_ligado = False
        self.__velocidade = 0.00

    def __del__(self):
        print("Objeto desalocado da memória!")

    @property
    def cor(self):
        return self._cor

    def detalhes(self):
        """Este método, exibe os detalhes do carro, todas os seus atributos."""
        print("******** DETALHES **************")
        print("Cor.............: ", self._cor)
        print("Tipo Combustível: ", self.__tipo_combustivel)
        print("Potência........: ", self.__potencia)
        print("Qtd. Combustível: ", self._qtd_combustivel)
        print("Velocidade......: ", self.__velocidade)
        if self.__is_ligado == True:
            print("Status..........: Ligado")
        else:
            print("Status..........: Desligado")
        print("********************************")

    def pintar(self, cor):
        self.__cor = cor

    def abastecer(self, qtd_combustivel):
        self.__qtd_combustivel += qtd_combustivel
        print("Abastecido!")

    def ligar(self):
        if self.__is_ligado == True:
            print("O veículo já está ligado...")
        else:
            self.__is_ligado = True
            print("Ligado!")

    def desligar(self):
        if self.__is_ligado == False:
            print("O veículo já está desligado...")
        else:
            self.__is_ligado = False
            self.__velocidade = 0
            print("Desligado!")

    # Definindo parametro padrão, caso nao seja passado
    def acelerar(self, velocidade=10):
        if self.__is_ligado == True:
            self.__velocidade += velocidade
            print("Velocidade aumentada!")
        else:
            print("O veículo precisa estar ligado...")