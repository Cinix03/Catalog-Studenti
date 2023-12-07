from Domain.StudentClass import Student
from Domain.StudentValidator import StudentValidator
from Repository.StudentRepo import StudentRepository
import random


class StudentService:
    def __init__(self, repo_stud, valid_stud):
        self.__repo_stud = repo_stud
        self.__valid_stud = valid_stud

    def add_student(self, id_student, nume):
        """
        Adauga studentul in memorie
        :param id_student: int
        :param nume: string
        :return:
        """
        student = Student(id_student, nume)
        self.__valid_stud.valideaza_student(student)
        self.__repo_stud.add_student(student)

    def delete_students(self, id_student):
        """
        sterge studentul
        :param id_student: int
        :return: -
        """
        student = Student(id_student, "Marcel")
        self.__valid_stud.valideaza_student(student)
        self.__repo_stud.delete_student(id_student)

    def modifica_student(self, id_student: int, nume_nou):
        """
        modifica studentul
        :param id_student: int
        :param nume_nou: string
        :return: -
        """
        student = Student(id_student, nume_nou)
        self.__valid_stud.valideaza_student(student)
        self.__repo_stud.modifica_student(student)

    def cauta_dupa_id(self, id_student):
        """
        cauta dupa id un student
        :param id_student: int
        :return: string
        """
        if not (id_student in self.__repo_stud.get_all_id()):
            raise Exception("Nu exista id-ul cerut!")
        return self.__repo_stud.get_nume_by_id(id_student)

    def cauta_dupa_nume(self, nume):
        """
        cauta dupa nume si returneaza id-urile
        :param nume: string
        :return: lista de id
        """
        if not (nume in self.__repo_stud.get_all()):
            raise Exception("Nu exista student cu acest nume")
        list_ids = self.__repo_stud.get_all_id()
        raspuns = []
        for x in list_ids:
            if self.__repo_stud.get_tot()[x] == nume:
                raspuns.append(x)
        return raspuns

    def creeaza_random(self, variante_nume: list, nr_ori):
        """

        :param variante_nume: lista de string
        :param nr_ori: int
        :return: -
        """
        while nr_ori:
            id_stud = random.randint(1, 200)
            nume = random.choice(variante_nume)
            student = Student(id_stud, nume)
            self.__valid_stud.valideaza_student(student)
            self.__repo_stud.add_student(student)
            nr_ori -= 1

    def get_all_students(self):
        """
        :return: lista cu toti studentii
        """
        return self.__repo_stud.get_all()
