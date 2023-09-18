from fastapi import APIRouter

router = APIRouter()


@router.get("/search/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/search/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/search/{username}")
async def read_user(username: str):
    return {"username": username}
