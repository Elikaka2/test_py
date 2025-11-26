from fastapi import APIRouter
from app.services.cats_service import get_cat_fact

router = APIRouter()

@router.get("/fact")
def get_cat_fact_endpoint():
    result = get_cat_fact()
    if "error" in result:
        return {"error": result["error"]}
    return result
