from course import Course


class Student:
    def __init__(self, id_num, courses):
        self.id_num = id_num
        self.courses = courses

    def insert_course(self, course):
        self.courses.append(course)

    @staticmethod
    def set_student_course_with_row(row, students_list, courses_list):
        student_index = Student.get_or_create_student_index_with_id(row[0], students_list)
        course = Course.get_specific_course_from_list(row[2], row[3], courses_list)
        students_list[student_index].insert_course(course)

    @staticmethod
    def get_or_create_student_index_with_id(id_num, students_list):
        index = Student.get_student_index_with_id(id_num, students_list)
        if index == -1:
            student = Student(id_num, [])
            students_list.append(student)
            index = len(students_list) - 1
        return index

    @staticmethod
    def get_student_index_with_id(id_num, students_list):
        for i in range(len(students_list)):
            if students_list[i].id_num == id_num:
                return i
        return -1
