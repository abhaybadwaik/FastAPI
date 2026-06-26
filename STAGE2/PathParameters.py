from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# ─────────────────────────────────────────
# PATH PARAMETERS
# ─────────────────────────────────────────

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "type": "path parameter"}

@app.get("/users/{user_id}/posts/{post_id}")
def get_user_post(user_id: int, post_id: int):
    return {"user_id": user_id, "post_id": post_id}

# ─────────────────────────────────────────
# QUERY PARAMETERS
# ─────────────────────────────────────────

@app.get("/products")
def get_products(category: str = "all", price: int = 0):
    return {"category": category, "price": price}

@app.get("/search")
def search(query: str, limit: int = 10, skip: int = 0):
    return {"query": query, "limit": limit, "skip": skip}

# ─────────────────────────────────────────
# REQUEST BODY
# ─────────────────────────────────────────

class User(BaseModel):
    name  : str
    email : str
    age   : int

class Product(BaseModel):
    title    : str
    price    : float
    in_stock : bool

@app.post("/users")
def create_user(user: User):
    return {"message": "User created!", "data": user}

@app.post("/products")
def create_product(product: Product):
    return {"message": "Product created!", "data": product}

# ─────────────────────────────────────────
# COMBINING PATH + QUERY TOGETHER
# ─────────────────────────────────────────

@app.get("/users/{user_id}/orders")
def get_user_orders(user_id: int, status: str = "all", limit: int = 5):
    return {
        "user_id" : user_id,
        "status"  : status,
        "limit"   : limit
    }

# ─────────────────────────────────────────
if __name__ == "__main__":
    uvicorn.run("PathParameters:app", host="0.0.0.0", port=8000, reload=True)