from fastapi import APIRouter
from .descriptive_stats import router as descriptor_stats_router
from .lexical_div import router as lexical_div_router
from .readability import router as readability_router
from .syntactical_complexity import router as syntactical_complexity_router

router = APIRouter()

router.include_router(descriptor_stats_router, prefix="/ds")
router.include_router(lexical_div_router, prefix="/lexical-div")
router.include_router(readability_router, prefix="/readability")
router.include_router(syntactical_complexity_router, prefix="/syntactical-complexity")