import unittest
from Utils.file_utils import clear_file_content, copy_file_content
from Repository.StudentRepo import StudentRepoFisier, StudentRepository
from Domain.StudentClass import Student


class StudentRepoTests(unittest.TestCase):
    def setUp(self):
        clear_file_content('StudTestRepo.txt')

    def test_add_student(self):
        test_repo = StudentRepository()
        self.assertEqual(test_repo.size(), 0)

        student = Student(1, "Mihai")
        test_repo.add_student(student)
        self.assertEqual(test_repo.size(), 1)
        with self.assertRaises(Exception):
            test_repo.add_student(student)

        student = Student(2, "George")
        test_repo.add_student(student)
        self.assertEqual(test_repo.size(), 2)
        with self.assertRaises(Exception):
            test_repo_add_student(student)

    def test_delete_student(self):
        test_repo = StudentRepository()
        self.assertEqual(test_repo.size(), 0)
        student = Student(1, "marcel")
        test_repo.add_student(student)
        self.assertEqual(test_repo.size(), 1)
        test_repo.delete_student(student.get_id_student())
        self.assertEqual(test_repo.size(), 0)
        test_repo.add_student(student)
        student = Student(2, "ion")
        test_repo.add_student(student)
        self.assertEqual(test_repo.size(), 2)
        with self.assertRaises(Exception):
            test_repo.delete_student(3)
        test_repo.delete_student(2)
        self.assertEqual(test_repo.size(), 1)

    def test_modifica_student(self):
        test_repo = StudentRepository()
        self.assertEqual(test_repo.size(), 0)
        student = Student(1, "ION")
        test_repo.add_student(student)
        self.assertEqual(test_repo.size(), 1)
        self.assertEqual(test_repo.get_nume_by_id(student.get_id_student()), "ION")
        test_repo.modifica_student(Student(1, "MIHAI"))
        self.assertEqual(test_repo.get_nume_by_id(student.get_id_student()), "MIHAI")

    def test_read_from_file(self):
        copy_file_content('studd.txt', 'StudTestRepo.txt')
        test_repo = StudentRepoFisier('StudTestRepo.txt')
        self.assertEqual(test_repo.size(), 3)

    def test_add_student_file(self):
        copy_file_content('studd.txt', 'StudTestRepo.txt')
        test_repo = StudentRepoFisier('StudTestRepo.txt')
        test_repo.add_student(Student(4, "Ghe"))
        self.assertEqual(test_repo.size(), 4)

    def test_delete_student_file(self):
        copy_file_content('studd.txt', 'StudTestRepo.txt')
        test_repo = StudentRepoFisier('StudTestRepo.txt')
        test_repo.delete_student(3)
        self.assertEqual(test_repo.size(), 2)

    def test_modifica_student_file(self):
        copy_file_content('studd.txt', 'StudTestRepo.txt')
        test_repo = StudentRepoFisier('StudTestRepo.txt')
        test_repo.modifica_student(Student(1, "Irinel"))
        self.assertEqual(test_repo.get_nume_by_id(1), "Irinel")
        with self.assertRaises(Exception):
            test_repo.modifica_student(Student(6, "dsadsa"))




