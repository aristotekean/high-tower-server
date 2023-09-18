from typing import Union
from starlette.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from apps.search.routes import router as SearchRoutes

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


# Routes
app.include_router(SearchRoutes, prefix="/search", tags=["search"])

origins = ["*"]
app = CORSMiddleware(
    app=app,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)