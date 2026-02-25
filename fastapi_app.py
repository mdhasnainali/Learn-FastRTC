from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from webcam_streem import stream

app = FastAPI()
stream.mount(app)

# Optional: Add routes
@app.get("/")
async def _():
    return HTMLResponse(content=open("index.html").read())

# This will also generate a Simple UI for Direct Test
# uvicorn fastapi_app:app --host 0.0.0.0 --port 8000