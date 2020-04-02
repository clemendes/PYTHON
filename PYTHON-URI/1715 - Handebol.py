# URI 1715
# CLEVERSON MENDES FARIA

# LOGICA UTILIZADA
# LER 2 ENTRADAS INICIAL (N) E (M) CORRESPONDENTE:
# N = NUMERO DE JGOADORES M = NUMERO DE PARTIDAS

entradas = input().split() # SEPARA AS ENTRADAS APOS O ESPAÇO

N = int(entradas[0]) # NUMERO DE JOGADORES
M = int(entradas[1]) # NUMERO DE PARTI

# PARA RANGE DE (N) DEVERÁ SER LIDO (M) GOLS EM CADA PARTIDA

gol_em_todos = 0

for i in range(N):
    entradas = input().split()

    jogos_com_gol = 0

    for i in entradas:
        if int(i) > 0:
             jogos_com_gol += 1

    if jogos_com_gol == M:
        gol_em_todos += 1

print(gol_em_todos)
