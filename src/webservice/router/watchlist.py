from fastapi import APIRouter

router = APIRouter()


@router.get("/rechercher_film/{recherche}")
async def rechercher_film(recherche):
    return
