from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome FastAPI"}

@app.get("/about")
def about():
    return {"about":"This website is about e-commerce"}

@app.get("/connect")
def connect():
  return {"connect":"This website is connecting"}

@app.get("/flipkart")
def flipkart():
    return {"message": "Welcome to Flipkart"}