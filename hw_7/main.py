from sqlalchemy import func, select, desc

from db_tables_creation import Grades, Groups, Students, Lecturers, Courses
from db_connection import session


# SELECT student_id , student_name , AVG(grades.grade) AS sort_avg FROM students
# LEFT JOIN grades ON students.student_id = grades.g_student_id
# GROUP BY student_id
# ORDER BY sort_avg DESC
# LIMIT 5

def query_1():
    db_selection = session.query(Students.student_id, Students.student_name, func.round(func.avg(Grades.grade)) \
                                 .label('avg_grade')) \
        .select_from(Students).join(Grades).group_by(Students.student_id).order_by(desc('avg_grade')).limit(5).all()
    return db_selection


# SELECT g_student_id, students.student_name, g_course_name, MAX(grade) AS Higher_grade FROM grades
# LEFT JOIN students ON grades.g_student_id = students.student_id
# LEFT JOIN courses ON grades.g_course_name = courses.course_name
# WHERE courses.course_id = 2

def query_2():
    db_selection = session.query(Grades.g_student_id, Students.student_name, Grades.g_course_id,
                                 func.max(Grades.grade).label('Higher_grade')).select_from(Grades).join(Students).join(
        Courses).filter(
        Courses.course_id == 2)
    return db_selection


# SELECT groups.group_name, students.student_name, g_course_name, AVG(grade) AS AVG_GRADE FROM grades
# LEFT JOIN students ON grades.g_student_id = students.student_id
# LEFT JOIN courses ON grades.g_course_name = courses.course_name
# LEFT JOIN groups ON grades.g_student_id = groups.student_member_group
# WHERE courses.course_id = 1 AND groups.group_name LIKE "%group - A%"

def query_3():
    db_selection = session.query(Groups.group_name, Students.student_name, Grades.g_course_id, func.avg(Grades.grade) \
                                 .label('AVG_GRADE')).select_from(Grades).join(Students).join(Groups).join(Courses).filter(
        Courses.course_id == 2, Groups.group_name == "group - A")
    return db_selection


if __name__ == '__main__':
    # a = query_1()
    # print('________________________________________QUERY # 1________________________________________')
    # for i in a:
    #    print(i)
    # print('_________________________________________________________________________________________')

    rtr = query_3()
    for i in rtr:
        print(i)
