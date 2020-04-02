# URI 2031
# CLEVERSON MENDES FARIA

n = int(input())

ataque = "ataque"
pedra = "pedra"
papel = "papel"

for i in range(0,n,1):

    player1 = str(input())
    player2 = str(input())

    if (player1 == ataque) and ((player2 == pedra) or (player2 == papel)):
        print("Jogador 1 venceu")
    elif (player1 == ataque) and (player2 == ataque):
        print("Aniquilacao mutua")
    elif (player2 == ataque) and ((player1 == pedra) or (player1 == papel)):
        print("Jogador 2 venceu")
    elif (player1 == pedra) and (player2 == papel):
        print("Jogador 1 venceu")
    elif (player2 == pedra) and (player1 == papel):
        print("Jogador 2 venceu")
    elif (player1 == pedra) and (player2 == pedra):
        print("Sem ganhador")
    elif (player1 == papel) and (player2 == papel):
        print("Ambos venceram")
