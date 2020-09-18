class Student:
    # 코드를 쓰세요
    def __init__(self, name, id, major):
        self.name = Name(name)
        self.id = Id(id)
        self.major = Major(major)
        self.grade = Grade()

    def print_report(self):
        print("코드잇 대학 성적표\n")


class Name:
    def __init__(self, name):
        self.name = name

    def change_student_name(self, new_name):
        self.name = new_name

    def print_report(self):
        print(f"학생 이름:{self.name}")


class Id:
    def __init__(self, id):
        self.id = id
        
    def change_student_id(self, new_id):
        self.id = new_id

    def print_report(self):
        print(f"학생 번호:{self.id}")


class Major:
    def __init__(self, major):
        self.major = major

    def change_student_major(self, new_major):
        self.major = new_major

    def print_report(self):
        print(f"소속 학과:{self.major}")


class Grade:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산 메소드"""
        return sum(self.grades) / len(self.grades)

    def print_report(self):
        print(f"평균 학점:{sum(self.grades) / len(self.grades)}")


# 작성한 클래스에 맞춰서 실행 코드도 바꿔보세요
# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.id.change_student_id(20130024)
younghoon.major.change_student_major("컴퓨터 공학과")

# 학생 성적 추가
younghoon.grade.add_grade(3.0)
younghoon.grade.add_grade(3.33)
younghoon.grade.add_grade(3.67)
younghoon.grade.add_grade(4.3)

# 학생 성적표 
younghoon.print_report()
younghoon.name.print_report()
younghoon.id.print_report()
younghoon.major.print_report()
younghoon.grade.print_report()