from fastapi import FastAPI

# Create a FastAPI app instance
app = FastAPI()

# Define a test route
@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI project!"}

@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}
