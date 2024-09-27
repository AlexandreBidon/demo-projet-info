from fastapi import APIRouter

router = APIRouter(
    prefix="/movie",
)


@router.get("/search/")
async def rechercher_film(query: str):
    return None


@router.get("/{movie_id}")
async def get_movie_by_id(movie_id: int):
    return None
