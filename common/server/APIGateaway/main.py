from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import httpx
import uvicorn


app = FastAPI()

SERVICE1_URL = "http://localhost:8001"
SERVICE2_URL = "http://localhost:8002"


@app.get("/api/resource/{item_id}")
async def read_item(item_id: int):
    
    if item_id % 2 == 0:
        service_url = SERVICE1_URL
    else:
        service_url = SERVICE2_URL 
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{service_url}/foo1/{item_id}")
            response.raise_for_status()
            return JSONResponse (content=response.json(), status_code=response.status_code)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=503, detail=str(e))
    