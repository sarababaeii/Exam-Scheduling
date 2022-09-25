week_days = {"شنبه": 1, "يکشنبه": 2, "دوشنبه": 3, "سه شنبه": 4, "چهارشنیه": 5, "پنجشنبه": 6, "جمعه": 7}


class Course:
    def __init__(self, id_num, code, group, days):
        self.id_num = id_num
        self.code = code
        self.group = group
        self.days = days

    @staticmethod
    def create_course_from_row(row):
        return Course(row[0], row[1], row[3], Course.create_running_days(row))

    @staticmethod
    def create_running_days(row):
        days = []
        for i in range(4, 6):
            if row[i] != "":
                days.append(Course.create_week_day_from_string(row[i]))
        return days

    @staticmethod
    def create_week_day_from_string(time):
        components = time.split("[")
        return week_days[components[0]]

    @staticmethod
    def get_specific_course_from_list(code, group, courses):
        for course in courses:
            if course.code == code and course.group == group:
                return course
        return None
