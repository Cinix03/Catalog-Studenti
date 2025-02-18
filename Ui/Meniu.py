from colorama import Fore
from Controller.StudentService import StudentService
from Controller.DisciplinaService import DisciplineService
from Controller.NotaService import NotaService


class UI:

    def __init__(self, service_students, service_disciplina, service_note):
        self.__service_students = service_students
        self.__service_disciplina = service_disciplina
        self.__service_note = service_note
        self.__commands = {
            "adauga_student": self.__ui_add_student,
            "print_students": self.__ui_print_students,
            "sterge_student": self.__ui_delete_student,
            "modifica_nume": self.__ui_modifica_nume,
            "adauga_disciplina": self.__ui_adauga_disciplina,
            "sterge_disciplina": self.__ui_sterge_disciplina,
            "print_discipline": self.__ui_print_discipline,
            "modifica_disciplina": self.__ui_modifica_disciplina,
            "cauta_disciplina_dupa_id": self.__ui_caut_disciplina_id,
            "cauta_disciplina_dupa_nume": self.__ui_cauta_disciplina_nume,
            "cauta_student_dupa_id": self.__ui_cauta_student_id,
            "cauta_student_dupa_nume": self.__ui_cauta_student_nume,
            "arata_note_student": self.__ui_arata_note_student,
            "adauga_note_student": self.__ui_adauga_nota_student,
            "adauga_studenti_random": self.__ui_adauga_random_studenti,
            "ordoneaza_studenti_alfabetic": self.__ui_ordoneaza_studenti_alfabetic,
            "ordoneaza_studenti_note": self.__ui_ordoneaza_studenti_note,
            "ordoneaza_studenti_medii": self.__ui_ordoneaza_studenti_medii,
        }

    def __ui_ordoneaza_studenti_medii(self, params):
        if len(params) != 0:
            raise Exception("nr parametri invalid")
        print(self.__service_note.get_primii_20())

    def __ui_adauga_random_studenti(self, params):
        if len(params) != 1:
            raise Exception("Nr parametri invalid")
        try:
            cati_studenti = int(params[0])
        except ValueError:
            print("Nu ati introdus un numar")
        variante_nume = ["Alex", "Gabi", "Traian", "Serbanescu", "Ionut"]
        self.__service_students.creeaza_random(variante_nume, cati_studenti)

    def __ui_adauga_nota_student(self, params):
        if len(params) != 3:
            raise Exception("Nr parametri invalid!")
        try:
            id_student = int(params[0])
            id_disc = int(params[1])
            nota = int(params[2])
        except ValueError:
            print("Nu au fost introdusi parametrii corect")
        self.__service_note.add_nota(id_student, id_disc, nota)

    def __ui_arata_note_student(self, params):
        if len(params) != 1:
            raise Exception("Nr parametri invalid")
        try:
            id = int(params[0])
        except ValueError:
            print("Nu ati introdus un id valid")
        print(self.__service_note.get_note_student(id))

    def __ui_print_students(self, params):
        if len(params) != 0:
            print("nr parametri invalid!")
            return
        students = self.__service_students.get_all_students()
        for student in students:
            print(student)

    def __ui_add_student(self, params):
        if len(params) != 2:
            print("nr parametri invalid sefule!")
            return
        try:
            id_student = int(params[0])
            name = params[1]
        except ValueError:
            raise Exception("valoare numerica invalida")
        self.__service_students.add_student(id_student, name)
        print("student adaugat cu succes!")

    def __ui_delete_student(self, params):
        if len(params) != 1:
            print("nr parametri invalid!")
            return
        try:
            id_student = int(params[0])
        except ValueError:
            raise Exception("Valoare numerica invalida")
        self.__service_students.delete_students(id_student)

    def __ui_modifica_nume(self, params):
        if len(params) != 2:
            print("nr parametri invalid!")
            return
        try:
            id_student = int(params[0])
            nume_nou = params[1]
        except ValueError:
            raise Exception("Valoare numerica invalida")
        self.__service_students.modifica_student(id_student, nume_nou)

    def __ui_adauga_disciplina(self, params):
        if len(params) != 3:
            print("nr invalid de parametri")
            return
        try:
            id_disc = int(params[0])
            nume_disc = params[1]
            profesor = params[2]
        except ValueError:
            raise Exception("Valoare numerica incorecta")
        self.__service_disciplina.add_disciplina(id_disc, nume_disc, profesor)

    def __ui_print_discipline(self, params):
        if len(params) != 0:
            print("Numar parametri invalid")
            return
        discipline = self.__service_disciplina.get_all()
        for x in discipline:
            print(x)

    def __ui_sterge_disciplina(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        try:
            disciplina = int(params[0])
        except ValueError:
            raise Exception("Valoare numerica gresit introdusa")
        self.__service_disciplina.delete_disciplina(disciplina)

    def __ui_modifica_disciplina(self, params):
        if len(params) != 3:
            print("Numar parametri invalid")
            return
        try:
            id_disc = int(params[0])
            numee = params[1]
            profesorr = params[2]
        except ValueError:
            raise Exception("Valoare numerica gresit introdusa")
        self.__service_disciplina.modifica_disciplina(id_disc, numee, profesorr)

    def __ui_caut_disciplina_id(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        else:
            try:
                id_disc = int(params[0])
            except ValueError:
                raise Exception("Valoare numerica gresit introdusa")
        print(self.__service_disciplina.caut_disciplina_id(id_disc))

    def __ui_cauta_disciplina_nume(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        else:
            try:
                nume = params[0]
            except ValueError:
                raise Exception("Nume incorect")
        print(self.__service_disciplina.cauta_disciplina_nume(nume))

    def __ui_cauta_student_id(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        else:
            try:
                id_student = int(params[0])
            except ValueError:
                raise Exception("Valoare numerica gresit introdusa!")
        print(self.__service_students.cauta_dupa_id(id_student))

    def __ui_cauta_student_nume(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        else:
            print(self.__service_students.cauta_dupa_nume(params[0]))

    def __ui_ordoneaza_studenti_alfabetic(self, params):
        if len(params) != 1:
            raise Exception("Nr parametri invalid")
        try:
            discip = int(params[0])
        except ValueError:
            print("Nu ati introdus un numar")
        self.__service_note.get_ordine_alfabetica(discip)

    def __ui_ordoneaza_studenti_note(self, params):
        if len(params) != 1:
            raise Exception("Nr parametri invalid")
        try:
            discip = int(params[0])
        except ValueError:
            print("Nu ati introdus un numar")
        print(self.__service_note.get_ordine_note(discip))

    def run(self):
        while True:
            cmd = input(">>>")
            cmd = cmd.strip()
            if cmd == "exit":
                return
            parts = cmd.split(" ")
            cmd_name = parts[0]
            params = parts[1:]
            if cmd_name in self.__commands:
                try:
                    self.__commands[cmd_name](params)
                except Exception as ex:
                    print(ex)
            else:
                print("Comanda invalida")


