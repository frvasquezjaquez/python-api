from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/fvasquez")
async def root():
    return {
        "name": "Francisco",
        "email": "francisco.vasquez@intec.edu.do",
        "clase": "DevOps" 
     }    