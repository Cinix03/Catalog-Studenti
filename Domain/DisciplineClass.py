class Disciplina:
    def __init__(self, id_disciplina, nume, profesor):
        self.__id_disciplina = id_disciplina
        self.__nume = nume
        self.__profesor = profesor

    def get_id_disciplina(self):
        return self.__id_disciplina

    def get_nume(self):
        return self.__nume

    def get_profesor(self):
        return self.__profesor

    def set_name(self, nume):
        self.__nume = nume

    def set_id_disciplina(self, id_disciplina):
        self.__id_disciplina = id_disciplina

    def set_profesor(self, profesor):
        self.__profesor = profesor

    def __eq__(self, other):
        return self.__id_disciplina == other.get_id_disciplina()
