from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Test"}

@app.get("/")
async def say_hello(name: str, message: str):
    return {"message": f"Hello {name}! {message}"}
