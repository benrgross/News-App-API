from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_news():
    return {"message": "List of news"}