import argparse
from sqlalchemy import func, select, desc, distinct

from db_tables_creation import Grades, Groups, Students, Lecturers, Courses
from db_connection import session


def query_1():
    db_selection = session.query(Students.student_id, Students.student_name, func.round(func.avg(Grades.grade)) \
                                 .label('avg_grade')) \
        .select_from(Students) \
        .join(Grades) \
        .group_by(Students.student_id) \
        .order_by(desc('avg_grade')).limit(5).all()
    return db_selection


# def query_2(): MAX не работает
#    db_selection = session.query(Grades.g_student_id, Students.student_name, Grades.g_course_id,
#                                 func.max(Grades.grade).label('Higher_grade')).select_from(Grades).join(Students).join(
#        Courses).filter(
#        Courses.course_id == 1).group_by(Grades.g_course_id).group_by(
#        Grades.g_student_id, Students.student_id)
#    return db_selection
def query_2():
    db_selection = session.query(Grades.g_student_id, Students.student_name, Grades.g_course_id,
                                 Grades.grade.label('Higher_grade')).select_from(Grades) \
        .join(Students).join(Courses) \
        .order_by(desc('Higher_grade')) \
        .filter(Courses.course_id == 1).limit(1)
    return db_selection


def query_3():
    db_selection = session.query(Groups.group_name, func.avg(Grades.grade)).select_from(Grades) \
        .group_by(Groups.group_name) \
        .filter(Groups.group_name == 'group - A')

    return db_selection


def query_4():
    db_selection = session.query(func.avg(Grades.grade).label('avg_course'))

    return db_selection


def query_5():
    db_selection = session.query(Courses.course_name, Courses.speaker, Lecturers.lecturer_name).select_from(Lecturers) \
        .join(Courses) \
        .filter(Lecturers.lecturer_id == 1) \
        .distinct(Courses.course_name)

    return db_selection


def query_6():
    db_selection = session.query(Students.student_name, Groups.group_name).select_from(Students) \
        .join(Groups) \
        .filter(Groups.group_name == 'group - B')
    return db_selection


def query_7():
    db_selection = session.query(Students.student_name, Grades.grade, Groups.group_name).select_from(Students) \
        .join(Groups).join(Grades) \
        .filter(Groups.group_name == 'group - B')
    return db_selection


def query_8():
    db_selection = session.query(func.round(func.avg(Grades.grade), 2).label('avg_grade from this guy'),
                                 Lecturers.lecturer_name) \
        .select_from(Students) \
        .join(Groups).join(Grades).filter(Groups.group_name == 'group - B', Lecturers.lecturer_id == 1) \
        .group_by(Lecturers.lecturer_id)
    return db_selection


def query_9():
    db_selection = session.query(Students.student_name, Courses.course_name).select_from(Grades) \
        .join(Students).join(Courses) \
        .filter(Students.student_name == 'Angela Davis                                      ')
    return db_selection


def query_10():
    db_selection = session.query(Courses.course_name) \
        .select_from(Grades) \
        .filter(Courses.speaker == 1,
                Students.student_name == 'Angela Davis                                       '). \
        distinct(Courses.course_name)

    return db_selection


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='Execute QYERY to DB Postgresql')
    parser.add_argument('-q', '--query_no', help='Enter No. of query(it can be from 1 to 10)')
    args = parser.parse_args()
    get_no = int(args.query_no)
    print(get_no)

    if get_no in range(1, 10):
        get_query = eval(f'query_{args.query_no}')
        response_db = get_query()

        for i in response_db:
            print(i)

    else:
        print('No. of query not detected, it shold be 1 - 10')
