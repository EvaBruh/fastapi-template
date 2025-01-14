import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/debug/")
def debug():
    return "debug message"


if "__name__" == "__main__":
    uvicorn.run("main:app", reload=True)
