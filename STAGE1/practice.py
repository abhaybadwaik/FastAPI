from fastapi import FastAPI
import uvicorn

app = FastAPI()

# ─────────────────────────────────────────
# GET → Fetch / Read data
# ─────────────────────────────────────────

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Practice!"}

@app.get("/users")
def get_users():
    return {
        "method"  : "GET",
        "action"  : "Fetching all users",
        "users"   : ["Abhay", "Rahul", "Priya"]
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "method"  : "GET",
        "action"  : "Fetching single user",
        "user_id" : user_id
    }

# ─────────────────────────────────────────
# POST → Create new data
# ─────────────────────────────────────────

@app.post("/users")
def create_user():
    return {
        "method"  : "POST",
        "action"  : "Creating a new user",
        "status"  : "User created successfully!"
    }

@app.post("/users/{user_id}/posts")
def create_user_post(user_id: int):
    return {
        "method"  : "POST",
        "action"  : "Creating post for user",
        "user_id" : user_id,
        "status"  : "Post created!"
    }

# ─────────────────────────────────────────
# PUT → Update entire data
# ─────────────────────────────────────────

@app.put("/users/{user_id}")
def update_user(user_id: int):
    return {
        "method"  : "PUT",
        "action"  : "Updating full user data",
        "user_id" : user_id,
        "status"  : "User fully updated!"
    }

# ─────────────────────────────────────────
# PATCH → Update partial data
# ─────────────────────────────────────────

@app.patch("/users/{user_id}")
def partial_update_user(user_id: int):
    return {
        "method"  : "PATCH",
        "action"  : "Updating partial user data",
        "user_id" : user_id,
        "status"  : "User partially updated!"
    }

# ─────────────────────────────────────────
# DELETE → Remove data
# ─────────────────────────────────────────

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {
        "method"  : "DELETE",
        "action"  : "Deleting user",
        "user_id" : user_id,
        "status"  : "User deleted successfully!"
    }

# ─────────────────────────────────────────
if __name__ == "__main__":
    uvicorn.run("practice:app", host="0.0.0.0", port=8000, reload=True)