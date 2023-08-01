from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db.db_sql import SessionLocal
from logic.user_actions import add_user, validate_user
from schema import SignupInfo

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


def get_db():
    db = None
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()


def check_signup_credential(username: str, password: str) -> bool:
    if len(username.strip()) < 4:
        return False
    if len(password.strip()) < 8:
        return False
    return True


@router.post("/signup")
async def signup(signup_info: SignupInfo, db: Session = Depends(get_db)):
    username = signup_info.username
    password = signup_info.password
    if check_signup_credential(username, password):
        action_status, token = add_user(username, password, db)
        if action_status == 1:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "hint": "user_signup_successful",
                    "code": 1,
                    "token": token
                }
            )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "hint": "something_went_wrong_during_signup",
            "code": 0
        }
    )


@router.get("/login")
async def login(username: str, password: str, db: Session = Depends(get_db)):
    token = validate_user(username, password, db)
    if token == "":
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "hint": "user_credentials_not_found",
                "code": 0
            }
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "hint": "login_successful",
            "code": 1,
            "token": token
        }
    )
