from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import httpx


app = FastAPI()

SERVICE1_URL = "http://service1:8001"
SERVICE2_URL = "httsp://service2:8002"


@app.get("api/resource/{item_id}")
async def read_item(item_id: int):
    
    service_url = SERVICE1_URL if item_id % 2 == 0 else SERVICE2_URL

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{service_url}/foo1/{item_id}")
            response.raise_for_status()
            return JSONResponse (content=response.json, status_code=response.status_code)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail= str(e))