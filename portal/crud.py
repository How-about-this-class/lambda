from sqlalchemy.orm import Session

import models
import schemas


def get_portal_by_major_lecture_name(db: Session, major: str, lecture_name: str):
    return (db.query(models.Portal)
            .filter_by(department=major, lecture_name=lecture_name)
            .all())


def get_portal_by_major_professor(db: Session, major: str, name: str):
    return (db.query(models.Portal)
            .filter_by(department=major)
            .join(models.Portal.professors)
            .filter_by(name=name).all())


def get_portal_page_by_major_multiple_lecture_name(db: Session, major: str, lecture_name: list[str], skip: int = 0,
                                                   limit: int = 10):
    return (db.query(models.Portal)
            .filter_by(department=major)
            .filter(models.Portal.lecture_name.in_(lecture_name))
            .order_by(models.Portal.option_5.desc())
            .offset(skip)
            .limit(limit)
            .all())


def get_portal_page_by_major(db: Session, major: str, skip: int = 0, limit: int = 10):
    return (db.query(models.Portal)
            .filter_by(department=major)
            .order_by(models.Portal.option_5.desc())
            .offset(skip)
            .limit(limit)
            .all())


def get_portal_page_by_multiple_lecture_name(db: Session, lecture_name: list[str], skip: int = 0, limit: int = 10):
    return (db.query(models.Portal)
            .filter(models.Portal.lecture_name.in_(lecture_name))
            .order_by(models.Portal.option_5)
            .offset(skip)
            .limit(limit)
            .all())


def get_portal_page(db: Session, skip: int = 0, limit: int = 10):
    return (db.query(models.Portal)
            .order_by(models.Portal.option_5)
            .offset(skip)
            .limit(limit)
            .all())
