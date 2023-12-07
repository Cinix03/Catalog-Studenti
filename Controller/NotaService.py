from Domain.NoteClass import Nota
from Domain.NotaValidator import NotaValidator
from Repository.NoteRepo import NotaRepository


class NotaService:
    def __init__(self, repo, valid, repo1, repo2):
        self.__repo_nota = repo
        self.__valid_nota = valid
        self.__repo_stud = repo1
        self.__repo_disc = repo2

    def add_nota(self, id_student, id_disciplina, nota):
        nota = Nota(id_student, id_disciplina, nota)
        if not (id_disciplina in self.__repo_disc.get_all_id()):
            raise Exception("Nu exista disciplina dorita!")
        if not (id_student in self.__repo_stud.get_all_id()):
            raise Exception("Nu exista studenti!")
        self.__valid_nota.valideaza_nota(nota)
        self.__repo_nota.add_nota(nota)

    def get_nota(self, id_stud, id_disc):
        return self.__repo_nota.get_nota_materie(id_stud, id_disc)

    def get_ordine_alfabetica(self, id_disc):
        studenti = self.__repo_stud.get_all_id()
        lista_cu_studenti_cu_note = []
        lista_note = []
        for x in studenti:
            if self.get_nota(x, id_disc) != 0:
                lista_cu_studenti_cu_note.append(self.__repo_stud.get_nume_by_id(x))
                lista_note.append(self.__repo_nota.get_nota_materie(x, id_disc))
        lista_cu_studenti_cu_note.sort()
        for i in range(0, len(lista_cu_studenti_cu_note)):
            print(str(lista_cu_studenti_cu_note[i]) + " " + str(lista_note[i]))

    def get_ordine_note(self, id_disc):
        studenti = list(self.__repo_stud.get_all_id())
        if len(studenti) == 0:
            raise Exception("Nu exista studenti")
        for x in range(0, len(studenti) - 1):
            for y in range(x + 1, len(studenti)):
                if self.__repo_nota.get_nota_materie(studenti[x], id_disc) < self.__repo_nota.get_nota_materie(
                        studenti[y], id_disc):
                    studenti[x], studenti[y] = studenti[y], studenti[x]
        rezultat = []
        for i in studenti:
            rezultat.append(str(self.__repo_stud.get_nume_by_id(i)) + " " + str(self.__repo_nota.get_nota_materie(i, id_disc)))
        return rezultat

    def get_primii_20(self):
        studenti = list(self.__repo_stud.get_all_id())
        discipline = list(self.__repo_disc.get_all_id())
        if len(studenti) < 5:
            raise Exception("Nu sunt suficienti oameni")
        medii = []
        for x in studenti:
            suma = 0
            for y in discipline:
                suma += self.__repo_nota.get_nota_materie(x, y)
            medii.append(int(suma/len(discipline)))
        for x in range(0, len(studenti)):
            for y in range(x, len(studenti)):
                if medii[x] < medii[y]:
                    medii[x], medii[y] = medii[y], medii[x]
                    studenti[x], studenti[y] = studenti[y], studenti[x]
        rezultat = []
        pana_la_cat = int(len(studenti)/5)
        for x in range(0, pana_la_cat):
            rezultat.append(str(self.__repo_stud.get_nume_by_id(studenti[x])) + ' ' + str(medii[x]))
        return rezultat

    def studentii_cu_nota_cea_mai_aproape_de_x(self, x, id_disc):
        studenti = list(self.__repo_stud.get_all_id())
        if len(studenti) == 0:
            raise Exception("Nu exista studenti")
        if not (id_disc in self.__repo_disc.get_all_id()):
            raise Exception("Nu exista id")
        cati_studenti = len(studenti)
        for i in range(0, cati_studenti):
            for j in range(i, cati_studenti):
                if abs(self.__repo_nota.get_nota_materie(studenti[i], id_disc)-x) > abs(self.__repo_nota.get_nota_materie(studenti[j], id_disc)-x):
                    studenti[i], studenti[j] = studenti[j], studenti[i]
        rezultat = []
        for i in range(0, cati_studenti):
            rezultat.append(str(self.__repo_stud.get_nume_by_id(studenti[i])) + ' ' + str(self.__repo_nota.get_nota_materie(studenti[i], id_disc)))
        return rezultat

    def get_note_student(self, id_student):
        return self.__repo_nota.get_note_student(id_student)
