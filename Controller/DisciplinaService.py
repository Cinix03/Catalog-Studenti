from Domain.DisciplineClass import Disciplina
from Repository.DisciplinaRepo import DisciplinaRepository
from Domain.DisciplinaValidator import DisciplinaValidator


class DisciplineService:
    def __init__(self, repo_disc, valid_disc):
        self.__repo_disc = repo_disc
        self.__valid_disc = valid_disc

    def add_disciplina(self, id_disciplina, nume_disciplina, profesor):
        disciplina = Disciplina(id_disciplina, nume_disciplina, profesor)
        self.__valid_disc.valideaza_disciplina(disciplina)
        self.__repo_disc.add_disciplina(disciplina)

    def delete_disciplina(self, id_disciplina):
        disciplina = Disciplina(id_disciplina, "mate", "matei")
        self.__valid_disc.valideaza_disciplina(disciplina)
        self.__repo_disc.delete_disciplina(id_disciplina)

    def modifica_disciplina(self, id_disciplina, nume, profesor):
        disciplina = Disciplina(id_disciplina, nume, profesor)
        self.__valid_disc.valideaza_disciplina(disciplina)
        self.__repo_disc.modifica_disciplina(id_disciplina, nume, profesor)

    def caut_disciplina_id(self, id_disciplina):
        if not (id_disciplina in self.__repo_disc.get_all_id()):
            raise Exception("Nu exista materie cu id-ul acesta")
        else:
            profesor = self.__repo_disc.get_brut()[id_disciplina][1]
            nume_disc = self.__repo_disc.get_brut()[id_disciplina][0]
            return f'Disciplina este {nume_disc}, iar numele profesorului este {profesor}'

    def cauta_disciplina_nume(self, nume):
        discipline = self.__repo_disc.get_all()
        if not (nume in self.__repo_disc.get_all_names()):
            raise Exception("Nu exista numele disciplinei dorite")
        else:
            raspuns = []
            discipline = self.__repo_disc.get_brut()
            for x in discipline.keys():
                if discipline[x][0] == nume:
                    raspuns.append([x, discipline[x][1]])
        return raspuns

    def get_all(self):
        return self.__repo_disc.get_all()
