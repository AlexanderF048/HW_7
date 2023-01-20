from sqlalchemy import Column, Integer, CHAR, ForeignKey, func, DateTime
from sqlalchemy.orm import relationship

from db_connection import Base, engine


class Grades(Base):
    __tablename__ = 'grades'
    grade_id = Column(Integer, primary_key=True, autoincrement=True)
    g_student_id = Column(CHAR(36), ForeignKey('students.student_id', onupdate="CASCADE", ondelete="CASCADE"))
    g_course_id = Column(Integer, ForeignKey('courses.course_id', onupdate="CASCADE", ondelete="CASCADE"))
    grade = Column(Integer)
    grade_time = Column(DateTime,
                        default=func.now())  # При использовании ф-ии. отбивает время создания а не старта сервера
    # -----------------------
    students_bridge = relationship('Students', back_populates='grades_bridge')
    courses_bridge = relationship('Courses', back_populates='grades_bridge')


class Groups(Base):
    __tablename__ = '[groups]'
    group_id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(CHAR(36))
    student_member_group = Column(CHAR(36), ForeignKey('students.student_id', onupdate="CASCADE", ondelete="CASCADE"))
    # -----------------------
    students_bridge = relationship('Students', back_populates='groups_bridge')


class Students(Base):
    __tablename__ = 'students'
    student_id = Column(CHAR(36), primary_key=True, nullable=False)
    student_name = Column(CHAR(50))
    # -------------------------
    groups_bridge = relationship('Groups', back_populates='students_bridge')
    grades_bridge = relationship('Grades', back_populates='students_bridge')


class Lecturers(Base):
    __tablename__ = 'lecturers'
    lecturer_id = Column(Integer, primary_key=True, autoincrement=True)
    lecturer_name = Column(CHAR(50))
    academic_degree = Column(CHAR(50))


class Courses(Base):
    __tablename__ = 'courses'
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(CHAR(50))
    speaker = Column(Integer, ForeignKey('lecturers.lecturer_id', onupdate="CASCADE", ondelete="CASCADE"))
    # -------------------------
    lecturers_bridge = relationship('Lecturers', backref='courses_bridge')  # backref - можно прописать единажды
    grades_bridge = relationship('Grades', back_populates='courses_bridge')


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
