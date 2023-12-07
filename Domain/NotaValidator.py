from Domain.NoteClass import Nota
from Repository.StudentRepo import StudentRepository
from Repository.DisciplinaRepo import DisciplinaRepository


class NotaValidator:

    def valideaza_nota(self, nota):
        erori = ""
        if nota.get_id_student() < 0 or nota.get_id_disciplina() < 0:
            erori += "id invalid!\n"
        if 1 > nota.get_nota() > 10:
            erori += "nota invalida!\n"
        if len(erori) > 0:
            raise Exception(erori)
