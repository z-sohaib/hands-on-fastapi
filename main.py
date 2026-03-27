from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: str = Field(default="", max_length=1000)
    price: float = Field(gt=0)
    in_stock: bool = True
    category: str = Field(default="general", min_length=2)

class ProductUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=1000)
    price: float | None = Field(default=None, gt=0)
    in_stock: bool | None = Field(default=None)
    category: str | None = Field(default=None, min_length=2)

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    in_stock: bool
    category: str

app = FastAPI()

# In-memory database
products_db: dict[int, dict] = {}
next_id = 1

# Path Types
# Static Paths: /products => Get All Products
# Parametered Paths: /products/{id} e.g: /products/qfeeqgfwrg265 => Get a Specific Product by ID
# Queried Paths: /products?in_stock=true&limit=10 => Get First 10 Products that are in stock

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]

@app.get("/products") # GET /products
def get_products(in_stock: bool | None = None, category: str | None = None):
    products_list = list(products_db.values())
    if in_stock is not None:
        products_list = [product for product in products_list if product["in_stock"] == in_stock]
    if category is not None:
        products_list = [product for product in products_list if product["category"] == category]
    return products_list

@app.post("/products", status_code=201) # POST /products
def create_product(product: Product):
    global next_id
    products_db[next_id] = product.model_dump()
    products_db[next_id]["id"] = next_id
    created_product = products_db[next_id]
    next_id += 1
    return {"message": "Product created successfully", "product": created_product}

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    products_db[product_id] = product.model_dump()
    return {"message": "Product updated successfully", "product": products_db[product_id]}

@app.patch("/products/{product_id}")
def patch_product(product_id: int, product: ProductUpdate):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    stored_product = products_db[product_id]
    patched_product = product.model_dump(exclude_unset=True)
    stored_product.update(patched_product)
    return {"message": "Product patched successfully", "product": stored_product}

@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    del products_db[product_id]
    return Response(status_code=204)