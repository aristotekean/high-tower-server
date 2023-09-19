import sys
import uvicorn
import motor
from fastapi import FastAPI
from beanie import init_beanie
from core.config import settings
from starlette.middleware.cors import CORSMiddleware

# Models
from apps.trends.schemas import UserBase, QueryBase

# Routes
from apps.search.routes import router as SearchRoutes
from apps.trends.routes import router as TrendsRoutes

DESCRIPTION = """

The API has the ability to search Torre.ai users.


You will be able to:

* **Search users**.

"""

app = FastAPI(
    title="High-Tower API",
    description=DESCRIPTION,
    version="0.0.1",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Home path
@app.get("/", summary="Health check", tags=["home"])
async def read_root():
    """_summary_

    Returns:
        _type_: _description_
    """
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn."
    return {"message": message}

@app.on_event("startup")
async def on_startup():
    """_summary_
    """
    client = motor.motor_asyncio.AsyncIOMotorClient(
        settings.DB_URL, uuidRepresentation="standard")

    db = client[settings.DB_NAME]

    await init_beanie(
        database=db,
        #Models
        document_models=[UserBase, QueryBase],
    )


# Routes
app.include_router(SearchRoutes, prefix="/search", tags=["search"])
app.include_router(TrendsRoutes, prefix="/trends", tags=["trends"])

origins = ["*"]
app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.SERVER_HOST,
        reload=settings.DEBUG_MODE,
        port=settings.SERVER_PORT,
    )