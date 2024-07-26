from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

# Veritabanı tablolarını oluştur
models.Base.metadata.create_all(bind=database.engine)

@app.post("/notes/", response_model=schemas.Note)
def create_note(note: schemas.NoteCreate, db: Session = Depends(database.get_db)):
    return crud.create_note(db=db, note=note)

@app.get("/notes/", response_model=list[schemas.Note])
def read_notes(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    notes = crud.get_notes(db, skip=skip, limit=limit)
    return notes

@app.get("/notes/{note_id}", response_model=schemas.Note)
def read_note(note_id: int, db: Session = Depends(database.get_db)):
    db_note = crud.get_note_by_id(db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@app.put("/notes/{note_id}", response_model=schemas.Note)
def update_note(note_id: int, note: schemas.NoteUpdate, db: Session = Depends(database.get_db)):
    db_note = crud.update_note(db, note_id=note_id, note=note)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@app.delete("/notes/{note_id}", response_model=schemas.Note)
def delete_note(note_id: int, db: Session = Depends(database.get_db)):
    db_note = crud.delete_note(db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note



