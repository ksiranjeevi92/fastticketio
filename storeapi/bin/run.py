import uvicorn

if __name__ == "main":
    uvicorn.run("storeapi.main:app --reload", host="0.0.0.0")
