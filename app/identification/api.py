from fastapi import FastAPI

app = FastAPI()

@app.post("/authenticate")
def authenticate(request_data):
    pass

@app.post("/register")
def register(request_data):
    pass

