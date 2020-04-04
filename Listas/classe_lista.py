class Lista():
    # METODO CONSTRUCTOR - CRIA UM VETOR COM A QTD. POSIÇÕES PASSADAS PARAMETRO
    # INICIALIZA O VETOR COM Nx POSIÇÕES [NONE]
    def __init__(self, tamanho=0):
        self.__tamanho = tamanho
        self.__elementos = [None] * tamanho
        self.__posicao = 0

    # METODO STR -> LISTAR OS ELEMENTOS DA LISTA
    def __str__(self):
        return ' '.join([str(i) for i in self.__elementos])

    # METODO LISTAR_ELEMENTOS -> LISTA TODOS OS ELEMENTOS
    def listar_elementos(self):
        return self.__elementos

    # METODO CONTEM -> VERIFICA SE EXISTE O ELEMENTO NA LISTA
    def contem(self, elemento):
        for i in range(0,self.tamanho_vetor()):
            temp = self.__elementos[i]
            if temp == elemento:
                return True
        return False

    # METODO INDICE -> RETORNA O INDICE DO ELEMENTO NA LISTA
    def indice(self, elemento):
        for i in range(0,self.tamanho_vetor()):
            temp = self.__elementos[i]
            if temp == elemento:
                return i
        return -1

    # METODO INSERIR_ELEMENTO_POSICAO
    def inserir_elemento_posicao(self, elemento, posicao):
        # 1, 2 , 3
        # Inserir_elemento_posicao(3,1)
        vetor_inicio = self.__elementos[:posicao] + [None]
        vetor_final = self.__elementos[posicao:]
        vetor_inicio[len(vetor_inicio)-1] = elemento
        self.__elementos = vetor_inicio + vetor_final
        self.__posicao += 1

    # METODO INSERIR_ELEMENTO_FINAL
    def inserir_elemento_final(self, elemento):
        self.__posicao = self.tamanho_vetor()
        if self.__posicao >= self.tamanho_vetor():
            self.__elementos = self.__elementos + [None]
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    # METODO TAMANHO_VETOR -> RETORNA O TAMANHO DA LISTA
    def tamanho_vetor(self):
        return len(self.__elementos)

    # APRESENTA MENU COM AS OPÇÕES DA LISTA
    def menu(self):
        print(" -  TRABALHANDO COM LISTAS  -")
        print(" -------- OPÇÕES ----------- ")
        print("[1] INSERIR REGISTRO NO FINAL")
        print("[2] INSERIR REGISTRO NA POSIÇÃO")
        print("[3] CONSULTAR REGISTRO")
        print("[4] EXIBIR TAMANHO DA LISTA")
        print("[5] LISTAR REGISTROS")
        print("[0] SAIR")