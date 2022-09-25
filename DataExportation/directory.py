from enum import Enum


class Directory(Enum):
    courses = 'Courses.csv'
    students_courses = 'List.csv'
    final_data = 'Data.csv'

    def __str__(self):
        return str(self.value)