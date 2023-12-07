class Nota:
    def __init__(self, id_student, id_disciplina, nota):
        self.__id_student = id_student
        self.__id_disciplina = id_disciplina
        self.__nota = nota

    def get_nota(self):
        return self.__nota

    def get_id_student(self):
        return self.__id_student

    def get_id_disciplina(self):
        return self.__id_disciplina

    def __eq__(self, other):
        return self.__id_student == other.get_id_student() and self.__id_disciplina == other.get_id_disciplina()
    
