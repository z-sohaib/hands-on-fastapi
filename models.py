from sqlmodel import SQLModel, Field

# Shared Parent Model
class ProductBase(SQLModel):
    name: str = Field(min_length=2, max_length=100)
    description: str = Field(default="", max_length=1000)
    price: float = Field(gt=0)
    in_stock: bool = True
    category: str = Field(default="general", min_length=2)

# DB Table
class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

# POST /products request body
class ProductCreate(ProductBase):
    pass

# PATCH /products request body
class ProductUpdate(SQLModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=1000)
    price: float | None = Field(default=None, gt=0)
    in_stock: bool | None = Field(default=None)
    category: str | None = Field(default=None, min_length=2)

# HTTP Response to product related endpoints
class ProductPublic(ProductBase):
    id: int


