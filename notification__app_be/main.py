from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def notify():
    return {"message":"Notification model"}