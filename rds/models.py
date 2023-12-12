from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, Table
from sqlalchemy.orm import relationship

from database import Base

portal_professor = Table(
    "portal_professor",
    Base.metadata,
    Column("id", BigInteger, primary_key=True),
    Column("portal_id", BigInteger, ForeignKey("portal.id")),
    Column("professor_id", BigInteger, ForeignKey("professor.id"))
)


class Portal(Base):
    __tablename__ = "portal"

    id = Column(BigInteger, primary_key=True, index=True)
    lecture_name = Column(String(50), index=True)
    department = Column(String(30))
    academic_number = Column(String(20))
    semester = Column(String(10))
    survey_cnt = Column(String(10))
    total_cnt = Column(String(10))
    option_1 = Column(String(10))
    option_2 = Column(String(10))
    option_3 = Column(String(10))
    option_4 = Column(String(10))
    option_5 = Column(String(10))
    detail_uk = Column(BigInteger)

    professors = relationship("Professor", secondary=portal_professor, back_populates="portals")


class Professor(Base):
    __tablename__ = "professor"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(15), index=True)

    portals = relationship("Portal", secondary=portal_professor, back_populates="professors")
