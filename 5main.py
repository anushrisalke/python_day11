from fastapi import FastAPI

app=FastAPI()

@app.get("/products/")

def get_product(limit:int =10):
    return{"limit":limit}


#new changes