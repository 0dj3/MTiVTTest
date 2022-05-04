from dataclasses import dataclass
from datetime import date
import re


@dataclass
class Student:
    fio: str
    code: int

    # Инициализация
    def __init__(self, value_fio: str, value_code: int):
        self.setFio(value_fio)
        self.setCode(value_code)

    # Задать ФИО
    def setFio(self, new_fio):
        # Проверка на тип
        if type(new_fio) != str:
            raise Exception("U vas wrong type")
        # Проверка введённых данных на ФИО
        pattern = '[A-ZА-ЯЁ][a-zа-яё]+\s+[A-ZА-ЯЁ][a-zа-яё]+(?:\s+[A-ZА-ЯЁ][a-zа-яё]+)?'
        if not re.fullmatch(pattern, new_fio):
            raise Exception("U vas incorrect input")
        self.fio = new_fio

    # Получить ФИО студента
    def getFio(self):
        return self.fio

    # Задать номер студента
    def setCode(self, new_code):
        # Проверка на тип
        if type(new_code) != int:
            raise Exception("U vas wrong type")
        # Проверка введённых данных на номер студента
        if not re.fullmatch(r'[1-9][0-9]{5}', str(new_code)):
            raise Exception("U vas incorrect input")
        self.code = new_code

    # Получить номер студента
    def getCode(self):
        return self.code


@dataclass
class Specialization:
    name: str

    # Инициализация
    def __init__(self, value_name: str):
        self.setName(value_name)

    # Задать название
    def setName(self, new_name):
        # Проверка типа
        if type(new_name) != str:
            raise Exception("U vas wrong type")
        # Проверка на правильность ввода названия
        if not re.fullmatch(r'[А-Я]+', new_name):
            raise Exception("U vas incorrect input")
        self.name = new_name

    # Получить название
    def getName(self):
        return self.name


@dataclass
class Group:
    name: str
    year: int
    spec: Specialization

    # Инициализация
    def __init__(self, value_spec: Specialization, value_year: int):
        self.setSpec(value_spec)
        self.setYear(value_year)
        self.setName(value_spec, value_year)

    # Задать год поступления?
    def setYear(self, new_year):
        # Проверка типа
        if type(new_year) != int:
            raise Exception("U vas wrong type")
        # Проверка на правильност ввода
        if not re.fullmatch(r'[0-9]{4}', str(new_year)):
            raise Exception("U vas incorrect input")
        self.year = new_year

    # Получить год поступления?
    def getYear(self):
        return self.year

    # Задать специализацию
    def setSpec(self, new_spec):
        # Проверка типа
        if type(new_spec) != Specialization:
            raise Exception("U vas wrong type")
        self.spec = new_spec

    # Получить специализацию
    def getSpec(self):
        return self.spec.name

    # Задать название группы
    def setName(self, spec, year):
        if type(spec) != Specialization and type(year) != int:
            raise Exception("4to-to poshlo ne tak v setName Group")
        self.name = spec.name + '-' + str(year)[-2:]

    def getName(self):
        return self.name


@dataclass
class Subject:
    code: str
    name: str
    semester: int
    hours: int
    spec: Specialization

    def __init__(self, value_code: str, value_name: str, value_semester: int,
                 value_hours: int, value_spec: Specialization):
        self.setCode(value_code)
        self.setName(value_name)
        self.setSemestr(value_semester)
        self.setHours(value_hours)
        self.setSpec(value_spec)

    def setCode(self, new_code):
        # Проверка типа
        if type(new_code) != str:
            raise Exception("U vas wrong type")
        # Проверка на правильност ввода
        if not re.fullmatch(r'[А-Я][0-9][.][А-Я][.][0-9]{2}', str(new_code)):
            raise Exception("U vas incorrect input")
        self.code = new_code

    def getCode(self):
        return self.code

    def setName(self, new_name):
        if type(new_name) != str:
            raise Exception("U vas wrong type")
        self.name = new_name

    def getName(self):
        return self.name

    def setSemestr(self, new_semestr):
        if type(new_semestr) != int:
            raise Exception("U vas wrong type")
        self.semester = new_semestr

    def getSemestr(self):
        return self.name

    def setHours(self, new_hours):
        if type(new_hours) != int:
            raise Exception("U vas wrong type")
        self.hours = new_hours

    def getHours(self):
        return self.hours

    def setSpec(self, new_spec):
        if type(new_spec) != Specialization:
            raise Exception("U vas wrong type")
        self.spec = new_spec

    def getSpec(self):
        return self.spec.name


@dataclass
class ExamPoints:
    student: Student
    inPoints: float
    examPoints: float
    exDate: date
    groupName: str
    subject: Subject

    def __init__(self, value_student: Student, value_inPoints: float,
                 value_examPoints: float, value_date: date, value_groupName: str,
                 value_subject: Subject):
        self.setStudent(value_student)
        self.setInPoints(value_inPoints)
        self.setExamPoints(value_examPoints)
        self.setExDate(value_date)
        self.setGroupName(value_groupName)
        self.setSubject(value_subject)

    def setInPoints(self, new_inPoints):
        if type(new_inPoints) != float:
            raise Exception("Konkretno wrong input")
        if 70.0 < new_inPoints:
            raise Exception("Fail s ballami mnogo")
        if 0.0 > new_inPoints:
            raise Exception("Fail s ballami malo")
        self.inPoints = new_inPoints

    def getInPoints(self):
        return self.inPoints

    def setExamPoints(self, new_examPoints):
        if type(new_examPoints) != float:
            raise Exception("Konkretno wrong input")
        if 30.0 < new_examPoints:
            raise Exception("Fail s ballami mnogo")
        if 0.0 > new_examPoints:
            raise Exception("Fail s ballami malo")
        self.examPoints = new_examPoints

    def getExamPoints(self):
        return self.examPoints

    def setStudent(self, new_student):
        if type(new_student) != Student:
            raise Exception("Konkretno wrong input")
        self.student = new_student

    def getStudent(self):
        return self.student

    def setExDate(self, exDate):
        if type(exDate) != date:
            raise Exception("Date ne date)")
        self.exDate = exDate

    def getExDate(self):
        return self.exDate

    def setGroupName(self, groupName):
        if type(groupName) != str:
            raise Exception("GroupName ne str)")
        if not re.fullmatch(r'([МБ]-)?[А-Я]+-[1-9][0-9]', groupName):
            raise Exception("U vas oshibka v nameGroup ejje")
        self.groupName = groupName

    def getGroupName(self):
        return self.groupName

    def setSubject(self, value_subject):
        if type(value_subject) != Subject:
            raise Exception("GroupName ne str)")
        self.subject = value_subject

    def getSubject(self):
        return self.subject


@dataclass
class Exam:
    subject: Subject
    examDate: date
    year: str
    lectFio: str
    group: Group

    def __init__(self, value_subject: Subject, value_examDate: date,
                 value_year: str, value_lectFio: str, value_group: Group):
        self.setSubject(value_subject)
        self.setExamDate(value_examDate)
        self.setYear(value_year)
        self.setLectFio(value_lectFio)
        self.setGroup(value_group)

    def setSubject(self, new_subject):
        if type(new_subject) != Subject:
            raise Exception("Konkretno wrong input")
        self.subject = new_subject

    def getSubject(self):
        return self.subject

    def setExamDate(self, new_examDate):
        if type(new_examDate) != date:
            raise Exception("Konkretno wrong input")
        self.examDate = new_examDate

    def getExamDate(self):
        return self.examDate

    def setYear(self, new_year):
        if type(new_year) != str:
            raise Exception("Konkretno wrong input")
        # if not re.fullmatch(r'[1-9]{4}-[1-9]{4}', new_year):
        #     raise Exception("Fail s godami")
        self.year = new_year

    def getYear(self):
        return self.year

    def setLectFio(self, new_lectFio):
        if type(new_lectFio) != str:
            raise Exception("Konkretno wrong input")
        pattern = '[A-ZА-ЯЁ][a-zа-яё]+\s+[A-ZА-ЯЁ][a-zа-яё]+(?:\s+[A-ZА-ЯЁ][a-zа-яё]+)?'
        if not re.fullmatch(pattern, new_lectFio):
            raise Exception("U vas incorrect input")
        self.lectFio = new_lectFio

    def setGroup(self, new_group):
        if type(new_group) != Group:
            raise Exception("Konkretno wrong input")
        self.group = new_group

    def getGroup(self):
        return self.group
