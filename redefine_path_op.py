# from fastapi import FastAPI

# app = FastAPI()

# # The first one will always be used since the path matches first.

# @app.get("/users")
# async def read_users():
#     return ["Rick", "Morty"]


# @app.get("/users")
# async def read_users2():
#     return ["Bean", "Elfo"]



from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(golu: ModelName):
    if golu is ModelName.alexnet:
        return {"model_name": golu, "message": "Deep Learning FTW!"}

    if golu.value == "lenet":
        return {"model_name": golu, "message": "LeCNN all the images"}

    return {"model_name": golu, "message": "Have some residuals"}