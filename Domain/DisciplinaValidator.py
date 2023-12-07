class DisciplinaValidator:

    def valideaza_disciplina(self, disciplina):
        erori = ""
        if disciplina.get_id_disciplina() < 0:
            erori += "id invalid!\n"
        if disciplina.get_nume() == "":
            erori += "nume invalid disciplina\n"
        if disciplina.get_profesor() == "":
            erori += "numer invalid profesor\n"
        if len(erori) > 0:
            raise Exception(erori)