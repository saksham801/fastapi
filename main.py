from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "success", "message": "FastAPI is running on the Edge!"}

# Cloudflare looks for this specific entry point
async def on_fetch(request, env):
    return await app(request, env)