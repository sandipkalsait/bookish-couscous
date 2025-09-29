class Student:
    def __init__(self):
        self.reg_no = None
        self.name = None

    def setData(self, reg_no, name):
        self.reg_no = reg_no
        self.name = name

    def getData(self):
        return self.reg_no, self.name


class Exam:
    def __init__(self):
        self.exam_no = None
        self.pattern = None
        self.semester = None

    def setData(self, exam_no, pattern, semester):
        self.exam_no = exam_no
        self.pattern = pattern
        self.semester = semester

    def getData(self):
        return self.exam_no, self.pattern, self.semester


class Result(Student, Exam):
    def __init__(self):
        Student.__init__(self)
        Exam.__init__(self)
        self.m1 = 0
        self.m2 = 0
        self.m3 = 0

    def setData(self, reg_no, name, exam_no, pattern, semester, m1, m2, m3):
        Student.setData(self, reg_no, name)
        Exam.setData(self, exam_no, pattern, semester)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def getData(self):
        student_data = Student.getData(self)
        exam_data = Exam.getData(self)
        return (student_data[0], student_data[1],
                exam_data[0], exam_data[1], exam_data[2],
                self.m1, self.m2, self.m3)

    def result(self):
        result = "\n----- Student Result -----\n"
        result += f"Reg No   : {self.reg_no}\n"
        result += f"Name     : {self.name}\n"
        result += f"Exam No  : {self.exam_no}\n"
        result += f"Pattern  : {self.pattern}\n"
        result += f"Semester : {self.semester}\n"
        result += f"Marks    : {self.m1}, {self.m2}, {self.m3}\n"
        total = self.m1 + self.m2 + self.m3
        result += f"Total    : {total}\n"
        result += f"Percentage: {total / 3:.2f}%\n"
        result += "--------------------------"
        return result


def driver():
    r1 = Result()
    r1.setData("R001", "Sandip", "EX123", "MCQ", 5, 85, 90, 88)
    print(r1.result())

    print("\nRaw data from getData():")
    print(r1.getData())


driver()
