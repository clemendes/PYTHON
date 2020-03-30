import classe_mae_veiculo

# CLASSE FILHA - HERANÇA
class Carro(classe_mae_veiculo.Veiculo):

    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_portas = qtd_portas

    def abastecer(self, qtd_combustivel):
        print("O método foi chamado a partir da classe Carro")
        self._qtd_combustivel += qtd_combustivel

    # Implementação abc - Metodo Abstrato
    def pintar(self, cor):
        if cor == "Preto":
            print("O carro não pode ser preto.")
        else:
            self._cor = cor