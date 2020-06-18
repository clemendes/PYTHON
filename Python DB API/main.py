from cliente import Cliente
from cliente_repositorio import ClienteRepositorio

# ----- CRIANDO OBJETO CLIENTE ------
cliente = Cliente('Cleverson', 29)

# INSERINDO UM CLIENTE
ClienteRepositorio.inserir_cliente(cliente)

# EDITANDO UM CLIENTE
cliente.nome = 'Paty'
cliente.idade = 32
ClienteRepositorio.editar_cliente(7,cliente) # VALOR ANTIGO (PATRICIA, 30)

# REMOVENDO UM CLIENTE
ClienteRepositorio.remover_cliente(1) # REMOVENDO CLIENTE 1 (FERNANDO,31)

# LISTANDO OS CLIENTES
ClienteRepositorio.listar_clientes()