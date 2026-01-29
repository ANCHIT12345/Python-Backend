# ASSIGNMENT 1: Smart Health Check API

from fastapi import FastAPI, Query, Path, Request, HTTPException
from datetime import datetime
import time

app = FastAPI()
START_TIME = time.time()

# API Endpoints

# GET /api/health

# Behavior:

#     Accept optional query param verbose=true|false
#     Default verbose=false

# Response when verbose=false

# {

#   "status": "UP"

# }

# Response when verbose=true

# {

#   "status": "UP",

#   "uptimeMinutes": 125,

#   "checkedAt": "2026-01-17T20:30:00"

# }

# Invalid Query Param

#     Return 400 Bad Request


@app.get("/api/health")
def health(verbose: bool = Query(False)):
    if not isinstance(verbose, bool):
        raise HTTPException(status_code=400, detail="Invalid query parameter")

    if not verbose:
        return {"status": "UP"}

    return {
        "status": "UP",
        "uptimeMinutes": int((time.time() - START_TIME) / 60),
        "checkedAt": datetime.now().isoformat()
    }



#  ASSIGNMENT 2: Server Time Converter API

# API Endpoints

# GET /api/time

# Query Params

#     format=iso|unix
#     Default: iso

# Response (iso)

# {

#   "serverTime": "2026-01-17T20:30:00"

# }

# Response (unix)

# {

#   "serverTime": 1705504200

# }

# Invalid Format

# {

#   "error": "Invalid time format"

# }

# Status: 400


@app.get("/api/time")
def server_time(format: str = Query("iso")):
    if format == "iso":
        return {"serverTime": datetime.now().isoformat()}
    elif format == "unix":
        return {"serverTime": int(time.time())}
    else:
        raise HTTPException(status_code=400, detail="Invalid time format")


# ASSIGNMENT 3: Application Info with Version Control

# API Endpoints

# GET /api/about

# Query Param

#     version

# If version matches:

# {

#   "appName": "Public Info API",

#   "version": "1.0",

#   "status": "SUPPORTED"

# }

# If version is outdated:

# {

#   "appName": "Public Info API",

#   "version": "0.8",

#   "status": "DEPRECATED"

# }

# Missing version param:

# {

#   "error": "Version parameter required"

# }

# Status: 400


@app.get("/api/about")
def about(version: str = Query(None)):
    if not version:
        raise HTTPException(status_code=400, detail="Version parameter required")

    status = "SUPPORTED" if version == "1.0" else "DEPRECATED"

    return {
        "appName": "Public Info API",
        "version": version,
        "status": status
    }

# ASSIGNMENT 4: Public Resource Checker API

# API Endpoints

# GET /api/resource/{resourceId}

# Valid resourceIds: 1–5

# Valid ID

# {

#   "resourceId": 3,

#   "available": true

# }

# Invalid ID

# {

#   "error": "Resource not found"

# }

# Status: 404


@app.get("/api/resource/{resource_id}")
def resource(resource_id: int = Path(...)):
    if 1 <= resource_id <= 5:
        return {
            "resourceId": resource_id,
            "available": True
        }

    raise HTTPException(status_code=404, detail="Resource not found")



# ASSIGNMENT 5: Request Inspector API 

# API Endpoints

# GET /api/request-info

# Return details about the request itself

# {

#   "method": "GET",

#   "path": "/api/request-info",

#   "queryParams": {

#     "debug": "true"

#   }

# }

# Rules:

#     Do not expose headers like Authorization
#     If debug=true, add timestamp


@app.get("/api/request-info")
def request_info(request: Request, debug: bool = False):
    data = {
        "method": request.method,
        "path": request.url.path,
        "queryParams": dict(request.query_params)
    }

    if debug:
        data["timestamp"] = datetime.now().isoformat()

    return data



# ASSIGNMENT 6 (Security ): Input Boundary API

# API Endpoints

# GET /api/calculate

# Query Params

#     a (int)
#     b (int)

# Valid Input

# {

#   "result": 15

# }

# Invalid Input

# {

#   "error": "Parameters must be integers"

# }

# Status: 400

# Missing Params

# {

#   "error": "Required parameters missing"

# }

# Status: 400


@app.get("/api/calculate")
def calculate(a: int = Query(None), b: int = Query(None)):
    if a is None or b is None:
        raise HTTPException(status_code=400, detail="Required parameters missing")

    return {"result": a + b}




