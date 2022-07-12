from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
# -------------------------------------------------------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------------------------------------------------------------------------------
@app.post("/notice/", response_model=schemas.NotesList)
def create_note(note: schemas.CreateNotes, db: Session = Depends(get_db)):
    return crud.create_notes_item(db=db, item=note)


# -------------------------------------------------------------------------------------------------
@app.put("/notice/{notice_id}")
def update_notes(notice_id: int,
                 note: schemas.PutNotes,
                 db: Session = Depends(get_db)):

    current_notice = crud.put_notes(db, notice_id=notice_id, item=note)
    return current_notice


# -------------------------------------------------------------------------------------------------
@app.get("/notice/", response_model=list[schemas.NotesList])
def read_notice(db: Session = Depends(get_db),
                is_public=Query(default=None),
                is_important=Query(default=None)):

    notes = crud.get_all_notes(db, is_public=is_public, is_important=is_important)
    return notes


# -------------------------------------------------------------------------------------------------
@app.get("/notice/{notice_id}", response_model=schemas.NotesList)
def read_detail_notice(notice_id: int, db: Session = Depends(get_db)):
    current_notice = crud.get_certain_notice(db, notice_id=notice_id)
    return current_notice


# -------------------------------------------------------------------------------------------------
@app.delete("/notice/{notice_id}", response_model=schemas.NotesList)
def delete_notice(notice_id: int, db: Session = Depends(get_db)):
    current_notice = crud.delete_notes(db, notice_id=notice_id)
    return current_notice

