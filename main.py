from typing import Union


from fastapi import FastAPI, UploadFile
from PIL import Image
import io
from pydantic import BaseModel

from app.model import predict

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/upload-file")
async def upload_file(file: Union[UploadFile, None] = None):
    if not file:
        return {"message": "No upload file sent"}

    content = await file.read()
    img = Image.open(io.BytesIO(content))

    return {"filename": file.filename, "prediction": predict(img)}
