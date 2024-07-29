from sqlalchemy.orm import Session
from . import crud, schemas, models


def get_notes(db: Session, skip: int = 0, limit: int = 10):

    return crud.get_notes(db, skip=skip, limit=limit)


def create_note(db: Session, note: schemas.NoteCreate):
    return crud.create_note(db, note)


def get_note_by_id(db: Session, note_id: int):
    db_note = crud.get_note_by_id(db, note_id)
    if db_note is None:
        raise ValueError("Note not found")
    return db_note


def update_note(db: Session, note_id: int, note: schemas.NoteUpdate):
    db_note = crud.get_note_by_id(db, note_id)
    if db_note is None:
        raise ValueError("Note not found")
    return crud.update_note(db, note_id, note)


def delete_note(db: Session, note_id: int):
    db_note = crud.get_note_by_id(db, note_id)
    if db_note is None:
        raise ValueError("Note not found")
    return crud.delete_note(db, note_id)
