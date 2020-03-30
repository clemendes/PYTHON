import classe_mae_veiculo, classe_filha_carro, classe_filha_moto

# UTILIZANDO METODOS -> HERDADOS E SOBRESCRITOS

# CRIANDO UM OBJETO DO TIPO CARRO
carro_azul = classe_filha_carro.Carro("Azul", "Gasolina", 3.0, 4)

# CRIANDO UM OBJETO DO TIPO MOTO
moto_vermelha = classe_filha_moto.Moto("Vermelha", "Gasolina", 1500, 2)

# UTILIZANDO METODO ABASTECER -> classe CARRO
carro_azul.abastecer(15)

# UTILIZANDO METODO ABASTECER -> classe MOTO
moto_vermelha.abastecer(6)

# UTILIZANDO METODO LIGAR -> classe CARRO
carro_azul.ligar()

# UTILIZANDO METODO LIGAR -> classe MOTO
moto_vermelha.ligar()

# UTILIZANDO METODO PINTAR -> classe CARRO
carro_azul.pintar("Vermelho")

# UTILIZANDO METODO PINTAR -> classe MOTO
moto_vermelha.pintar("Azul")

# UTILIZANDO METODO ACELERAR -> classe CARRO
carro_azul.acelerar(80)

# UTILIZANDO METODO ACELERAR -> classe MOTO
moto_vermelha.acelerar(40)

# UTILIZANDO METODO DETALHES -> EXIBE TODOS OS DETALHES -> classe CARRO
carro_azul.detalhes()

# UTILIZANDO METODO DETALHES -> EXIBE TODOS OS DETALHES -> classe MOTO
moto_vermelha.detalhes()

# UTILIZANDO UMA @PROPERTY -> CORRESPONDE AO GET
print(moto_vermelha.cor)