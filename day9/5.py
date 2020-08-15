from Person import Person
from Student import Student
from Teacher import Teacher


def main():
    stu = Student('Iceberry', 15, '初三')
    stu.study('数学')
    stu.watch_tv()
    t = Teacher('Alice', 38, '专家')
    t.teach('《Python程序设计》')
    t.watch_tv()


if __name__ == "__main__":
    main()
