from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"sasf": "rtjs"}

@app.get("/SomeMessage")
def mypage():
    return{"message":"aopsies"}