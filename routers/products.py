from fastapi import APIRouter, HTTPException, Response
from database import SessionDep
from models import ProductPublic, ProductCreate, Product, ProductUpdate
from sqlmodel import select

router = APIRouter()

@router.post("/", response_model=ProductPublic, status_code=201)
async def create_product(product: ProductCreate, session: SessionDep):
    db_product = Product.model_validate(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

@router.get("/", response_model=list[ProductPublic])
def get_products(session: SessionDep, in_stock: bool | None = None, category: str | None = None, offset: int = 0, limit: int | None = None):
    query = select(Product) # SELECT * FROM product
    if in_stock is not None:
        query = query.where(Product.in_stock == in_stock) # SELECT * FROM product WHERE in_stock = true
    if category is not None:
        query = query.where(Product.category == category) # SELECT * FROM product WHERE category = 'some_category'
    
    products = session.exec(query.offset(offset).limit(limit)).all()
    return products

@router.get("/{product_id}", response_model=ProductPublic)
def get_product_by_id(product_id: int, session: SessionDep):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return product

@router.patch("/{product_id}", response_model=ProductPublic)
def update_product(product_id: int, product: ProductUpdate, session: SessionDep):
    product_to_update = session.get(Product, product_id)
    if not product_to_update:
        raise HTTPException(status_code=404, detail="Product not found")
    
    updated_data = product.model_dump(exclude_unset=True)
    product_to_update.sqlmodel_update(updated_data)
    session.add(product_to_update)
    session.commit()
    session.refresh(product_to_update)
    return product_to_update

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, session: SessionDep):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    session.delete(product)
    session.commit()
    return Response(status_code=204)
    