from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from utils import github_utils

app = FastAPI()


@app.get("/users")
async def home(request: Request):
    # Get params
    params = dict(request.query_params)

    usernames = params.get("usernames")
    include = params.get("include")
    if usernames:
        usernames = usernames.split(",")

    if usernames is None:
        data = {
            "error": {
                "message": "use - /users?usernames={comma},{separated},{usernames}"
            }
        }
    else:
        data = await github_utils(usernames, include)
    return JSONResponse(content=data)
