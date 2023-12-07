from Domain.StudentClass import Student


class StudentRepository:
    def __init__(self):
        self.__students = {}

    def add_student(self, student):
        id_student = student.get_id_student()
        nume_student = student.get_nume()
        if id_student in self.__students:
            raise Exception("id existent!\n")
        self.__students[id_student] = nume_student

    def delete_student(self, id_student):
        if not (id_student in self.__students.keys()):
            raise Exception("Id inexistent")
        for student in self.__students.keys():
            if student == id_student:
                self.__students.pop(student)
                break

    def modifica_student(self, student):
        if not (student.get_id_student() in self.__students.keys()):
            raise Exception("Id inexistent")
        for x in self.__students.keys():
            if x == student.get_id_student():
                self.__students[x] = student.get_nume()
                break

    def get_nume_by_id(self, id_student):
        return self.__students[id_student]

    def get_all(self):
        return [self.__students[x] for x in self.__students.keys()]

    def get_all_id(self):
        return list(self.__students.keys())

    def get_tot(self):
        return self.__students

    def size(self):
        return len(self.get_all_id())


class StudentRepoFisier(StudentRepository):
    def __init__(self, filename):
        StudentRepository.__init__(self)
        self.__filename = filename
        self.load_from_file()

    def load_from_file(self):
        with open(self.__filename, mode="r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                id_stud, nume_stud = line.split(' ')
                id_stud = int(id_stud.strip())
                nume_stud = nume_stud.strip()
                StudentRepository.add_student(self, Student(id_stud, nume_stud))

    def add_student(self, student: Student):
        StudentRepository.add_student(self, student)
        self.write_to_file()

    def delete_student(self, id_student):
        StudentRepository.delete_student(self, id_student)
        self.write_to_file()

    def modifica_student(self, student):
        StudentRepository.modifica_student(self, student)
        self.write_to_file()

    def write_to_file(self):
        ids = StudentRepository.get_all_id(self)
        nume_id = [str(iden) + ' ' + StudentRepository.get_nume_by_id(self, iden) for iden in ids]
        with open(self.__filename, mode="w", encoding="utf-8") as f:
            text_to_write = '\n'.join(nume_id)
            f.write(text_to_write)





