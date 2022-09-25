import csv
from directory import Directory
from course import Course
from student import Student


def read_from_csv(file_name):
    rows = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            rows.append(row)
        return [header, rows]


def set_courses():
    courses_dict = read_from_csv(Directory.courses.value)[1]
    courses = []
    for row in courses_dict:
        course = Course.create_course_from_row(row)
        courses.append(course)
    return courses


def set_students(courses):
    students_dict = read_from_csv(Directory.students_courses.value)[1]
    students = []
    for row in students_dict:
        Student.set_student_course_with_row(row, students, courses)
    return students


def write_data_to_csv(file_name, courses, students):
    write_set_to_csv(file_name, ["courses"], courses)
    write_set_to_csv(file_name, ["students"], students)
    write_courses_time_to_csv(file_name, courses)
    write_students_courses_to_csv(file_name, students)


def write_set_to_csv(file_name, field_name, array):
    with open(file_name, mode='a') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_name)
        writer.writeheader()
        for i in range(len(array)):
            writer.writerow({field_name[0]: array[i].id_num})


def write_courses_time_to_csv(file_name, courses):
    with open(file_name, mode='a') as csv_file:
        field_names = ["i", "k", "b(i, k)"]
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for course in courses:
            for day in course.days:
                writer.writerow({"i": course.id_num,
                                 "k": day,
                                 "b(i, k)": 1})


def write_students_courses_to_csv(file_name, students):
    with open(file_name, mode='a') as csv_file:
        field_names = ["i", "j", "a(i, j)"]
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for student in students:
            for course in student.courses:
                writer.writerow({"i": course.id_num,
                                 "j": student.id_num,
                                 "a(i, j)": 1})


if __name__ == '__main__':
    print("Hello World!")
    courses_list = set_courses()
    students_list = set_students(courses_list)
    write_data_to_csv(Directory.final_data.value, courses_list, students_list)
    # for course in courses_list:
    #     print(course.num, course.code, course.group, course.days)
    # for student in students_list:
    #     print(student.id_num, student.courses)
