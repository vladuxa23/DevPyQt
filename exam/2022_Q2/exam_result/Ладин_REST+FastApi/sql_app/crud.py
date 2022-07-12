from sqlalchemy import and_
from sqlalchemy import update
from sqlalchemy.orm import Session

from . import models, schemas


# -------------------------------------------------------------------------------------------------
def get_certain_notice(db: Session, notice_id: int):
    """
    Method for getting certain object
    :param db:db.connection
    :param notice_id: object id
    :return: None or object
    """
    return db.query(models.Notes).filter(models.Notes.id == notice_id).first()


# -------------------------------------------------------------------------------------------------
def create_notes_item(db: Session, item: schemas.CreateNotes):
    """
    Method for create new item in database
    :param db: db.connection
    :param item: schema of pydantic for creating object
    :return: sql_app.models.Notes
    """
    db_item = models.Notes(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# -------------------------------------------------------------------------------------------------
def put_notes(db: Session, notice_id: int, item: schemas.PutNotes):
    """
    Method for update item in database
    :param db: db.connection
    :param notice_id: object id
    :param item: schema of pydantic for updating object
    :return:
        - queue - empty result of query
        - result - sql_app.models.Notes
    """
    queue = db.query(models.Notes).filter(models.Notes.id == notice_id).first()
    if queue is None:
        return queue

    query = update(models.Notes).where(models.Notes.id == notice_id).values(
        status=item.status,
        is_public=item.is_public,
        is_important=item.is_important
    )

    result = execute_query(db=db, query=query)

    db.commit()

    return result


# -------------------------------------------------------------------------------------------------
def delete_notes(db: Session, notice_id: int):
    """
    Method for delete item in database
    :param db: db.connection
    :param notice_id: object id
    :return: sql_app.models.Notes
    """
    query = db.query(models.Notes).filter(models.Notes.id == notice_id).first()
    if query is None:
        return query
    db.delete(query)
    db.commit()
    return query


# -------------------------------------------------------------------------------------------------
def get_scalar_result(result):
    """
    :return: list of sql results
    """
    return [item for item in result.scalars()]


# -------------------------------------------------------------------------------------------------
def execute_query(db, query):
    """
    Method for executing query
    :param db: db.connection
    :param query: sql query
    :return: sql result
    """
    return db.execute(query)


# -------------------------------------------------------------------------------------------------
def get_all_notes(db: Session, is_public: int = None, is_important: int = None):
    """
    Method for getting result list of objects
    :param db: db.connection
    :param is_public: variable for sql query
    :param is_important: variable for sql query
    :return: sql result
    """
    if is_public and is_important:
        query = db.query(models.Notes).where(and_(models.Notes.is_public == 1,
                                                  models.Notes.is_important == 1))
        result = execute_query(db=db, query=query)
        return get_scalar_result(result)

    if is_public:
        query = db.query(models.Notes).where(models.Notes.is_public == 1)
        result = execute_query(db=db, query=query)
        return get_scalar_result(result)

    if is_important:
        query = db.query(models.Notes).where(models.Notes.is_important == 1)
        result = execute_query(db=db, query=query)
        return get_scalar_result(result)

    return db.query(models.Notes).all()
