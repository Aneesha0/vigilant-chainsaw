from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Anjana": "Hello Nai!!"}

@app.get("/SomeMessage")
def mypage():
    return{"message":"aopsies"}