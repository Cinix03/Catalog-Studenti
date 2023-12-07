from Domain.NoteClass import Nota


class NotaRepository:
    def __init__(self):
        self.__note = [[0 for col in range(2000)] for row in range(2000)]

    def add_nota(self, nota):
        self.__note[nota.get_id_student()][nota.get_id_disciplina()] = nota.get_nota()

    def get_nota_materie(self, id_student, id_materie):
        return self.__note[id_student][id_materie]

    def get_note_student(self, id_student):
        return self.__note[id_student]


class NotaRepoFisier(NotaRepository):
    def __init__(self, file_name):
        NotaRepository.__init__(self)
        self.__filename = file_name
        self.load_from_file()

    def load_from_file(self):
        with open(self.__filename, mode='r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                id_stud, id_disc, nota = line.split(' ')
                id_stud = int(id_stud.strip())
                id_disc = int(id_disc.strip())
                nota = int(nota.strip())
                NotaRepository.add_nota(self, Nota(id_stud, id_disc, nota))

    def add_nota(self, nota: Nota):
        NotaRepository.add_nota(self, nota)
        self.write_in_file()

    def write_in_file(self):
        lista = []
        for i in range(0, 2000):
            for j in range(i, 2000):
                if NotaRepository.get_nota_materie(self, i, j) != 0:
                    lista.append(str(i)+' '+str(j)+' '+str(NotaRepository.get_nota_materie(self, i, j)))
        with open(self.__filename, mode='w', encoding='utf-8') as f:
            text_to_write = '\n'.join(lista)
            f.write(text_to_write)





