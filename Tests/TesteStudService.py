import unittest
from Utils.file_utils import clear_file_content, copy_file_content
from Controller.StudentService import StudentService
from Domain.StudentClass import Student
from Repository.StudentRepo import StudentRepository, StudentRepoFisier
from Domain.StudentValidator import StudentValidator


class StudentServiceTests(unittest.TestCase):
    def setUp(self):
        clear_file_content('StudTestRepo.txt')

    def test_add_student(self):
        test_repo = StudentRepository()
        test_validator = StudentValidator()
        test_service = StudentService(test_repo, test_validator)
        test_service.add_student(1, "Marcel")
        self.assertEqual(test_repo.size(), 1)
        test_service.add_student(2, "MIADA")
        self.assertEqual(test_repo.size(), 2)
        with self.assertRaises(Exception):
            test_service.add_student(-5, "IDSADA")

    def test_delete_student(self):
        test_repo = StudentRepository()
        test_validator = StudentValidator()
        test_service = StudentService(test_repo, test_validator)
        test_service.add_student(1, "Marcel")
        self.assertEqual(test_repo.size(), 1)
        test_service.delete_students(1)
        self.assertEqual(test_repo.size(), 0)
        with self.assertRaises(Exception):
            test_service.delete_students(1)

    def test_modifica_student(self):
        test_repo = StudentRepository()
        test_validator = StudentValidator()
        test_service = StudentService(test_repo, test_validator)
        test_service.add_student(1, "Daniel")
        self.assertEqual(test_repo.size(), 1)
        with self.assertRaises(Exception):
            test_service.modifica_student(2, "nimic")

    def test_cauta_dupa_id_student(self):
        test_repo = StudentRepository()
        test_validator = StudentValidator()
        test_service = StudentService(test_repo, test_validator)
        test_service.add_student(1, "Daniel")
        self.assertEqual(test_repo.size(), 1)
        self.assertEqual(test_service.cauta_dupa_id(1), "Daniel")
        with self.assertRaises(Exception):
            test_service.cauta_dupa_id(20)

    def test_cauta_dupa_nume(self):
        test_repo = StudentRepository()
        test_validator = StudentValidator()
        test_service = StudentService(test_repo, test_validator)
        test_service.add_student(1, "Daniel")
        self.assertEqual(test_service.cauta_dupa_nume("Daniel"), [1])
        test_service.add_student(2, "Daniel")
        self.assertEqual(test_service.cauta_dupa_nume("Daniel"), [1, 2])




