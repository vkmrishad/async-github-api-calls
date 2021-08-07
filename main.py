from aiohttp import web

from utils import github_utils


async def home(request):
    # Get params
    params = request.rel_url.query

    usernames = params.get("usernames")
    include = params.get("include")
    if usernames:
        usernames = usernames.split(",")
    data = await github_utils(usernames, include)
    return web.json_response(data)

# Server
app = web.Application()
app.add_routes([web.get("/", home)])
web.run_app(app)