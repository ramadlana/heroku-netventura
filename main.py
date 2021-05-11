from _typeshed import OpenTextModeUpdating
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World1", "this":"from github"}


@app.get("/items/{item_id}-{nama}")
def read_item(item_id: int, q: Optional[str] = None, name: Optional[str]=None):
    return {"item_id": item_id, "q": q, "say": "halo {nama}"}