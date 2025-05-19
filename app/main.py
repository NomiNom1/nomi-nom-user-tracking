from fastapi import FastAPI

app = FastAPI(title="Nomi Nom User Tracking")

@app.get("/")
async def root():
    return {"message": "Hello World"} 