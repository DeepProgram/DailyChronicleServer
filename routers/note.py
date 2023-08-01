from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
import time
from logic.note_actions import process_and_add_notes, process_and_get_notes, process_and_update_notes, \
    process_and_delete_note
from schema import NoteInfo
from db.db_sql import SessionLocal
from logic.json_web_token import oauth2_bearer

router = APIRouter(
    prefix="/note",
    tags=["Note"]
)


def get_db():
    db = None
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()


@router.post("/add")
async def add_notes(note_info: NoteInfo, token: str = Depends(oauth2_bearer),
                    db: Session = Depends(get_db)):
    note_title = note_info.note_title
    note_body = note_info.note_body
    added_time = int(time.time())
    result = process_and_add_notes(note_title, note_body, added_time, token, db)
    if result == -1:
        return HTTPException(
            status_code=401,
            detail="token_invalid"
        )
    elif result == 0:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "hint": "database_error",
                "code": 0
            }
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "hint": "note_add_successful",
                "code": 1
            }
        )


@router.get("/view")
async def view_notes(token: str = Depends(oauth2_bearer), db: Session = Depends(get_db)):
    result, note_list = process_and_get_notes(token, db)
    if result == -1:
        return HTTPException(
            status_code=401,
            detail="token_invalid"
        )
    elif result == 0:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "hint": "notes_not_found",
                "code": 0
            }
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "hint": "notes_found",
                "code": 1,
                "notes": note_list
            }
        )


@router.put("/update")
async def note_update(note_info: NoteInfo, note_id: int, token: str = Depends(oauth2_bearer),
                      db: Session = Depends(get_db)):
    note_title = note_info.note_title
    note_body = note_info.note_body
    modification_time = int(time.time())
    result = process_and_update_notes(note_id, note_title, note_body, modification_time, token, db)

    if result == -1:
        return HTTPException(
            status_code=401,
            detail="token_invalid"
        )
    elif result == 0:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "hint": "database_error",
                "code": 0
            }
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "hint": "notes_updated",
                "code": 1,
            }
        )


@router.delete("/delete")
async def note_delete(note_id: int, token: str = Depends(oauth2_bearer),
                      db: Session = Depends(get_db)):
    result = process_and_delete_note(note_id, token, db)
    if result == -1:
        return HTTPException(
            status_code=401,
            detail="token_invalid"
        )
    elif result == 0:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "hint": "database_delete_operation_failed",
                "code": 0
            }
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "hint": "note_deleted",
                "code": 1,
            }
        )
