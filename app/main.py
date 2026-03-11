from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException, Request

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/time")
def get_time(request: Request):
    if request.headers.get("X-Debug") == "fail":
        raise HTTPException(status_code=500, detail="Forced failure")
    return {"utc_time": datetime.now(timezone.utc).isoformat()}