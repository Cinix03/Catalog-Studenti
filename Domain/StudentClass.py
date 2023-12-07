class Student:
    def __init__(self, id_student, nume):
        self.__id_student = id_student
        self.__nume = nume

    def get_id_student(self):
        """
        :return:id-ul studentului curent
        """
        return self.__id_student

    def get_nume(self):
        """

        :return: returneaza numele studentului curent
        """
        return self.__nume

    def set_name(self, nume):
        """

        :param nume: string cu numele studentului
        :return: ii schimba numele
        """
        self.__nume = nume

    def set_id_student(self, id_student):
        """

        :param id_student:
        :return: seteaza id-ul
        """
        self.__id_student = id_student

    def __eq__(self, other):
        return self.__id_student == other.__id_student

