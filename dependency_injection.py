from typing import Annotated
from fastapi import Depends, FastAPI
app = FastAPI()

async def common_parameter(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q":q, "slip": skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameter)]):
    return commons
@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameter)]):
    return commons