import classe_mae_veiculo

# CLASSE FILHA - HERANÇA
class Moto(classe_mae_veiculo.Veiculo):

    def __init__(self, cor, tipo_combustivel, potencia, qtd_passageiros):
        super().__init__(cor, tipo_combustivel, potencia)
        self.qtd_passageiros = qtd_passageiros

    def abastecer(self, qtd_combustivel):
        print("O método foi chamado a partir da classe Moto")
        if self._qtd_combustivel >= 30:
            print("O tanque está cheio!")
        else:
            self._qtd_combustivel += qtd_combustivel

    # Implementação abc - Metodo Abstrato
    def pintar(self, cor):
        if cor == "Preto" or cor == "Preta":
            print("A moto não pode ser preta.")
        else:
            self._cor = cor