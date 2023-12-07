from Domain.DisciplineClass import Disciplina


class DisciplinaRepository:
    def __init__(self):
        self.__discipline = {}

    def add_disciplina(self, disciplina):
        id_disciplina = disciplina.get_id_disciplina()
        nume_disciplina = disciplina.get_nume()
        profesor_disciplina = disciplina.get_profesor()
        if id_disciplina in self.__discipline:
            raise Exception("id existent!\n")
        self.__discipline[id_disciplina] = [nume_disciplina, profesor_disciplina]

    def delete_disciplina(self, id_disciplina):
        if not (id_disciplina in self.__discipline.keys()):
            raise Exception("Id inexistent")
        self.__discipline.pop(id_disciplina)

    def modifica_disciplina(self, id_disciplina, nume, profesor):
        if not (id_disciplina in self.__discipline.keys()):
            raise Exception("Id inexistent")
        self.__discipline[id_disciplina] = [nume, profesor]

    def get_all_id(self):
        return self.__discipline.keys()

    def get_all_names(self):
        rezultat = [self.__discipline[x][0] for x in self.__discipline.keys()]
        return rezultat

    def get_all(self):
        rezultat = [self.__discipline[x] for x in self.__discipline.keys()]
        return rezultat

    def get_brut(self):
        return self.__discipline


class DisciplinaRepoFisier(DisciplinaRepository):
    def __init__(self, file_name):
        DisciplinaRepository.__init__(self)
        self.__filename = file_name
        self.load_from_file()

    def load_from_file(self):
        with open(self.__filename, mode="r", encoding="utf-8") as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines if line.strip() != '']
            for line in lines:
                iden, nume_disc, nume_prof = line.split(' ')
                iden = int(iden.strip())
                nume_disc = nume_disc.strip()
                nume_prof = nume_prof.strip()
                DisciplinaRepository.add_disciplina(self, Disciplina(iden, nume_disc, nume_prof))

    def add_disciplina(self, disciplina: Disciplina):
        DisciplinaRepository.add_disciplina(self, disciplina)
        self.write_to_file()

    def delete_disciplina(self, id_disciplina):
        DisciplinaRepository.delete_disciplina(self, id_disciplina)
        self.write_to_file()

    def modifica_disciplina(self, id_disciplina, nume, profesor):
        DisciplinaRepository.modifica_disciplina(self, id_disciplina, nume, profesor)
        self.write_to_file()

    def write_to_file(self):
        ids_and_all = DisciplinaRepository.get_all_id(self)
        ids_and_all = [str(iden) + ' ' + str(DisciplinaRepository.get_brut(self)[iden][0]) + ' ' + str(DisciplinaRepository.get_brut(self)[iden][1]) for iden in ids_and_all]
        with open(self.__filename, mode='w', encoding='utf-8') as f:
            text_to_write = '\n'.join(ids_and_all)
            f.write(text_to_write)
