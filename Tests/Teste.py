import sys

from Domain.StudentClass import Student
from Domain.DisciplineClass import Disciplina
from Repository.StudentRepo import StudentRepository
from Repository.DisciplinaRepo import DisciplinaRepository
from Repository.NoteRepo import NotaRepository, NotaRepoFisier
from Domain.NoteClass import Nota
from Utils.file_utils import clear_file_content, copy_file_content
from Controller.NotaService import NotaService
from Domain.NotaValidator import NotaValidator


class Test:
    def test_create_student(self):
        primul_student = Student(34, "Damian")
        primul_student.set_id_student(245)
        assert primul_student.get_id_student() == 245
        assert primul_student.get_nume() == "Damian"

    def test_create_disciplina(self):
        prima_disciplina = Disciplina(3213, "Matematica", "Alexandru")
        prima_disciplina.set_id_disciplina(208)
        prima_disciplina.set_name("Istorie")
        prima_disciplina.set_profesor("Marcel")
        assert prima_disciplina.get_id_disciplina() == 208
        assert prima_disciplina.get_nume() == "Istorie"
        assert prima_disciplina.get_profesor() == "Marcel"

    def test_add_stud(self):
        nou_student = Student(34, "Georgian")
        studrep = StudentRepository()
        studrep.add_student(nou_student)
        assert studrep.get_all() == ["Georgian"]
        nou_student = Student(1, "Mihai")
        studrep.add_student(nou_student)
        assert studrep.get_all() == ["Georgian", "Mihai"]

    def test_delete_stud(self):
        nou_student = Student(34, "Georgian")
        studrep = StudentRepository()
        studrep.add_student(nou_student)
        assert studrep.get_all() == ["Georgian"]
        studrep.delete_student(34)
        assert studrep.get_all() == []

    def test_modifica_stud(self):
        nou_student = Student(34, "Georgian")
        nou_student_inlcuit = Student(34, "Gabriel")
        studrep = StudentRepository()
        studrep.add_student(nou_student)
        studrep.modifica_student(nou_student_inlcuit)
        assert studrep.get_all() == ["Gabriel"]

    def test_add_disc(self):
        noua_disciplina = Disciplina(1, "FP", "Istvanc")
        disc_rep = DisciplinaRepository()
        disc_rep.add_disciplina(noua_disciplina)
        assert disc_rep.get_all() == [["FP", "Istvanc"]]
        noua_disciplina = Disciplina(2, "FP", "Istvanc")
        disc_rep.add_disciplina(noua_disciplina)
        assert disc_rep.get_all() == [["FP", "Istvanc"], ["FP", "Istvanc"]]

    def test_delete_disc(self):
        noua_disciplina = Disciplina(1, "FP", "Istvanc")
        disc_rep = DisciplinaRepository()
        disc_rep.add_disciplina(noua_disciplina)
        assert disc_rep.get_all() == [["FP", "Istvanc"]]
        disc_rep.delete_disciplina(noua_disciplina.get_id_disciplina())
        assert disc_rep.get_all() == []

    def test_modifica_disc(self):
        noua_disciplina = Disciplina(1, "CS", "Istvanc")
        disc_rep = DisciplinaRepository()
        disc_rep.add_disciplina(noua_disciplina)
        assert disc_rep.get_all() == [["CS", "Istvanc"]]
        disc_rep.modifica_disciplina(1, "SS", "random")
        assert disc_rep.get_all() == [["SS", "random"]]
        noua_disciplina = Disciplina(5, "rada", "dasd")
        disc_rep.add_disciplina(noua_disciplina)
        disc_rep.modifica_disciplina(5, "altfel", "Ion")

    def test_adauga_nota(self):
        nou_student = Student(1, "George")
        noua_disciplina = Disciplina(1, "CS", "Istvanc")
        studrep = StudentRepository()
        discrep = DisciplinaRepository()
        notarep = NotaRepository()
        studrep.add_student(nou_student)
        discrep.add_disciplina(noua_disciplina)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 10)
        notarep.add_nota(nota)
        assert notarep.get_nota_materie(1, 1) == 10

    def test_get_ordine_note(self):
        nou_student = Student(1, "George")
        noua_disciplina = Disciplina(1, "CS", "Istvanc")
        studrep = StudentRepository()
        discrep = DisciplinaRepository()
        notarep = NotaRepository()
        studrep.add_student(nou_student)
        discrep.add_disciplina(noua_disciplina)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 10)
        notarep.add_nota(nota)
        nou_student = Student(2, "Marius")
        studrep.add_student(nou_student)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 7)
        notarep.add_nota(nota)
        nou_student = Student(3, "Ilie")
        studrep.add_student(nou_student)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 6)
        notarep.add_nota(nota)

        nou_student = Student(4, "Ariana")
        studrep.add_student(nou_student)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 5)
        notarep.add_nota(nota)

        nou_student = Student(5, "Ilinca")
        studrep.add_student(nou_student)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 5)
        notarep.add_nota(nota)
        notavalid = NotaValidator()

        notaserv = NotaService(notarep, notavalid, studrep, discrep)

        assert notaserv.get_ordine_note(1) == ["George 10", "Marius 7", "Ilie 6", "Ariana 5", "Ilinca 5"]

        studrep.delete_student(1)
        studrep.delete_student(2)
        studrep.delete_student(3)
        studrep.delete_student(4)
        studrep.delete_student(5)
        try:
            z = notaserv.get_ordine_note(1)
            assert False
        except Exception as error:
            assert str(error) == str("Nu exista studenti")


    def test_get_primii_20(self):
        nou_student = Student(1, "George")
        noua_disciplina = Disciplina(1, "CS", "Istvanc")
        studrep = StudentRepository()
        discrep = DisciplinaRepository()
        notarep = NotaRepository()
        studrep.add_student(nou_student)
        discrep.add_disciplina(noua_disciplina)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 10)
        notarep.add_nota(nota)
        nou_student = Student(2, "Marius")
        studrep.add_student(nou_student)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 7)
        notarep.add_nota(nota)
        nou_student = Student(3, "Ilie")
        studrep.add_student(nou_student)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 6)
        notarep.add_nota(nota)

        nou_student = Student(4, "Ariana")
        studrep.add_student(nou_student)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 5)
        notarep.add_nota(nota)

        nou_student = Student(5, "Ilinca")
        studrep.add_student(nou_student)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 5)
        notarep.add_nota(nota)
        notavalid = NotaValidator()

        notaserv = NotaService(notarep, notavalid, studrep, discrep)

        assert notaserv.get_primii_20() == ["George 10"]

    def test_studentii_cu_cea_mai_apropiata_nota_de_x(self):
        nou_student = Student(1, "George")
        noua_disciplina = Disciplina(1, "CS", "Istvanc")
        studrep = StudentRepository()
        discrep = DisciplinaRepository()
        notarep = NotaRepository()
        studrep.add_student(nou_student)
        discrep.add_disciplina(noua_disciplina)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 10)
        notarep.add_nota(nota)
        nou_student = Student(2, "Marius")
        studrep.add_student(nou_student)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 7)
        notarep.add_nota(nota)
        nou_student = Student(3, "Ilie")
        studrep.add_student(nou_student)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 6)
        notarep.add_nota(nota)

        nou_student = Student(4, "Ariana")
        studrep.add_student(nou_student)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 5)
        notarep.add_nota(nota)

        nou_student = Student(5, "Ilinca")
        studrep.add_student(nou_student)
        nota = Nota(nou_student.get_id_student(), noua_disciplina.get_id_disciplina(), 5)
        notarep.add_nota(nota)
        notavalid = NotaValidator()

        notaserv = NotaService(notarep, notavalid, studrep, discrep)

        assert notaserv.studentii_cu_nota_cea_mai_aproape_de_x(7, 1) == ["Marius 7", "Ilie 6", "Ariana 5", "Ilinca 5",
                                                                         "George 10"]
        try:
            z = notaserv.studentii_cu_nota_cea_mai_aproape_de_x(6, 20)
            assert False
        except Exception as error:
            assert str(error) == str("Nu exista id")

        studrep.delete_student(1)
        studrep.delete_student(2)
        studrep.delete_student(3)
        studrep.delete_student(4)
        studrep.delete_student(5)

        try:
            z = notaserv.studentii_cu_nota_cea_mai_aproape_de_x(10, 1)
            assert False
        except Exception as error:
            assert str(error) == str("Nu exista studenti")
