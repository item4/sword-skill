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
        data = orjson.loads(resp.content)
        result = {**data, "ok": True, "command": "weather"}
        print(orjson.dumps(result).decode("u8"))
