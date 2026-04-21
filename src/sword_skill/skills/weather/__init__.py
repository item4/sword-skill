from typing import Final

import orjson
from cyclopts import App
from httpx import AsyncClient

app = App(name="weather")

URL: Final = "https://item4.net/api/weather/"


@app.default
async def weather_command():
    async with AsyncClient() as client:
        resp = await client.get(URL)
        ok = resp.status_code == 200
        if ok:
            data = orjson.loads(resp.content)
        else:
            data = {"error": f"Bad HTTP Response: {resp.status_code}"}
        result = {**data, "ok": ok, "command": "weather"}
        print(orjson.dumps(result).decode("u8"))
