from random import randint, choice
import faker
from uuid import uuid4

from db_tables_creation import Grades, Groups, Students, Lecturers, Courses
from db_connection import session

UUID_BASE = []


def fake_lecturers(fake_object=faker.Faker()):
    degree = ('Dr.', 'Candidate of Science', 'Lead Engineer')

    for _ in range(3):
        lecturer = Lecturers(
            lecturer_name=fake_object.name(),
            academic_degree=choice(degree)
        )
        session.add(lecturer)
    session.commit()


def fake_courses(fake_object=faker.Faker()):
    for _ in range(3):
        course = Courses(
            course_name=fake_object.job(),
            speaker=randint(1, 3)
        )
        session.add(course)
    session.commit()


def fake_students(fake_object=faker.Faker()):
    for _ in range(10):
        id4stu = uuid4()
        student = Students(
            student_id=id4stu,
            student_name=fake_object.name()
        )
        UUID_BASE.append(id4stu)
        session.add(student)
    session.commit()


def fake_groups(fake_object=faker.Faker()):
    groups_example = ('group - A', 'group - B', 'group - C')

    for student_id in UUID_BASE:
        group = Groups(
            group_name=choice(groups_example),
            student_member_group=student_id
        )
        session.add(group)
    session.commit()


def fake_grades(fake_object=faker.Faker()):
    for i in range(1, 3+1):
        for student_id in UUID_BASE:
            grade = Grades(
                g_student_id=student_id,
                g_course_id=i,
                grade=randint(1, 100)
            )
            session.add(grade)
    session.commit()


if __name__ == "__main__":
    fake_lecturers()
    fake_courses()
    fake_students()
    fake_groups()
    fake_grades()

    UUID_BASE.clear()
