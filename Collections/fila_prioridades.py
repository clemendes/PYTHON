from queue import PriorityQueue

class Prioridades ():
    def get_estudantes(self,eventos):
        queue = PriorityQueue()
        for evento in eventos:
            if("ADICIONAR" in evento):
                dados = evento.split(" ")
                queue.put(Estudante(int(dados[3]), dados[1], float(dados[2])))
            else:
                queue.get()

        estudantes = []
        while (not queue.empty()):
            estudantes.append(queue.get())

        return estudantes

class Estudante ():

    def __init__(self, id, nome, nota):
        self.__id = id
        self.__nome = nome
        self.__nota = nota

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def nota(self):
        return self.__nota

    def __str__(self):
        return str(self.__id) + " - " + self.__nome + " - " + str(self.__nota)

    def __eq__(self, other):
        return ((self.__id, self.__nome, self.__nota) ==
                (other.id, other.nome, other.nota))
    def __lt__(self, other):
        if (self.__nota > other.nota):
            return True
        else:
            if (self.__nota == other.nota):
                if(self.__nome < other.nome):
                    return True
                else:
                    if(self.__nome == other.nome):
                        if(self.__id < other.id):
                            return True
        return False


if __name__ == "__main__":
    
    totalEventos = int(input())
    eventos = []
        
    for i in range(0,totalEventos):
        evento = input()
        eventos.append(evento)
        
    
    prioridades = Prioridades()
    estudantes = prioridades.get_estudantes(eventos)
        
    if (len(estudantes) == 0):
        print("VAZIO")
    else:
        for estudante in estudantes:
            print(estudante.nome)