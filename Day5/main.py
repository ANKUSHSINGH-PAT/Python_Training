from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items/")
async def read_item(name: str = None, price: float = None):
    return {"name": name, "price": price}



@app.get("/products/")
async def read_product(product_id: int):
    return {"product_id": product_id}


@app.get("/search/")
async def search(query: str = "default search", limit: int = 10):
    return {"query": query, "limit": limit}


@app.get("/filter/")
async def filter_items(category: str = "all", price_min: float = 0.0, price_max: float = 1000.0):
    return {"category": category, "price_range": [price_min, price_max]}


@app.post("/items/")
async def create_item(item: Item):
    return {"Laptop": item}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str = None):
    result = {"item_id": item_id, "item": item}
    if q:
        result["q"] = q
    return result




@app.get("/Items/{item_id}")
def read_item(item_id: int):
    if item_id < 1:
        raise HTTPException(status_code=400, detail="Item ID must be greater than 0")
    return {"item_id": item_id}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


@app.get("/downloadfile/")
async def download_file():
    file_path = "demo.txt"
    return FileResponse(file_path, media_type='application/octet-stream', filename="downloaded_file.txt")

