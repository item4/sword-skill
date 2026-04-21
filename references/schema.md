# Output Schema

## Common output rules

All commands must emit exactly one JSON object to stdout.

Common top-level fields:

- `ok: bool`
- `command: str`

On failure, the output includes `ok: false` and a top-level `error` field containing a human-readable error message.

`stderr` is reserved for logs or diagnostics and must not contain the primary result payload.

---

## `weather`

### Command

```shell
sws weather
```

### Success shape example

```json
{
"ok": true,
"command": "weather",
"observed_at": "2025-04-21T13:30:00+09:00",
"records": [{"id":90,"name":"속초","height":18,"rain":{"is_raining":"Clear","rain15":0.0,"rain60":0.0,"rain3h":0.0,"rain6h":0.0,"rain12h":0.0,"rainday":0.0},"temperature":21.7,"wind1":{"direction_code":260.0,"direction_text":"W","velocity":8.2},"wind10":{"direction_code":264.7,"direction_text":"W","velocity":7.7},"humidity":18.0,"atmospheric":1011.5,"address":"강원특별자치도 고성군 토성면 봉포리"}]
}
```

### Fields

- `ok`
    - Type: `true`
    - Meaning: the command succeeded

- `command`
    - Type: literal string `"weather"`
    - Meaning: identifies the subcommand that produced this output

- `observed_at`
    - Type: `str`
    - Format: ISO 8601 datetime string with timezone offset
    - Meaning: timestamp of the observation set represented by this payload

- `records`
    - Type: `list[Record]`
    - Meaning: list of station observation records across South Korea

### `Record` Shape

Represents one AWS station observation.

```json
{
    "id":90,
    "name":"속초",
    "height":18,
    "rain":{
        "is_raining":"Clear",
        "rain15":0.0,
        "rain60":0.0,
        "rain3h":0.0,
        "rain6h":0.0,
        "rain12h":0.0,
        "rainday":0.0
    },
    "temperature":21.7,
    "wind1":{
        "direction_code":260.0,
        "direction_text":"W",
        "velocity":8.2
    },
    "wind10":{
        "direction_code":264.7,
        "direction_text":"W",
        "velocity":7.7
    },
    "humidity":18.0,
    "atmospheric":1011.5,
    "address":"강원특별자치도 고성군 토성면 봉포리"
}
```
#### Fields

- `id`
    - Type: `int`
    - Meaning: Korea Meteorological Administration internal station ID

- `name`
    - Type: `str`
    - Meaning: AWS station name

- `height`
    - Type: `int`
    - Unit: meters
    - Meaning: elevation above sea level. `height` is always emitted as int by the current parser.

- `rain`
    - Type: `Rain`
    - Meaning: rain status and accumulated rainfall measurements

- `temperature`
    - Type: `int | float`
    - Unit: °C
    - Meaning: measured air temperature in Celsius

- `wind1`
    - Type: `Wind`
    - Meaning: 1-minute wind observation

- `wind10`
    - Type: `Wind`
    - Meaning: 10-minute wind observation

- `humidity`
    - Type: `int | float`
    - Unit: percent
    - Meaning: relative humidity

- `atmospheric`
    - Type: `int | float`
    - Unit: hPa
    - Meaning: atmospheric pressure in hectopascals

- `address`
    - Type: `str`
    - Meaning: station address


### `Rain` Shape

Represents rainfall-related fields for a station.

```json
{
    "is_raining": "Clear",
    "rain15": 0.0,
    "rain60": 0.0,
    "rain3h": 0.0,
    "rain6h": 0.0,
    "rain12h": 0.0,
    "rainday": 0.0
}
```

#### Fields

- `is_raining`
    - Type: `"Clear" | "Rain" | "Unavailable" | "Unknown"`
    - Meaning:
        - `Clear`: no rain currently detected
        - `Rain`: raining now (does not distinguish rain vs snow)
        - `Unavailable`: this AWS does not provide rain information
        - `Unknown`: unknown state for other reasons

- `rain15`
    - Type: `int | float`
    - Meaning: 15-minute rainfall amount
    - Unit: WIP (currently presumed by author, not yet formally verified)

- `rain60`
    - Type: `int | float`
    - Meaning: 60-minute rainfall amount
    - Unit: WIP

- `rain3h`
    - Type: `int | float`
    - Meaning: 3-hour rainfall amount
    - Unit: WIP

- `rain6h`
    - Type: `int | float`
    - Meaning: 6-hour rainfall amount
    - Unit: WIP

- `rain12h`
    - Type: `int | float`
    - Meaning: 12-hour rainfall amount
    - Unit: WIP

- `rainday`
    - Type: `int | float`
    - Meaning: daily accumulated rainfall
    - Unit: WIP

- Note: These rainfall units are not yet formally verified and should not be treated as authoritative.

### `Wind` Shape

Represents wind observation data.

```json
{
    "direction_code": 260.0,
    "direction_text": "W",
    "velocity": 8.2
}
```

#### Fields

- `direction_code`
    - Type: `int | float`
    - Meaning: numeric wind direction code in decimal form

- `direction_text`
    - Type: `str`
    - Meaning: cardinal/intercardinal wind direction label such as `N`, `S`, `NE`, `SSW`

- `velocity`
    - Type: `int | float`
    - Unit: m/s
    - Meaning: wind speed

### Note

- Numeric measurement fields are documented as int | float for practical downstream consumption.

## Failure shape example

```json
{
    "ok": false,
    "command": "weather",
    "error": "Bad HTTP Response: 503"
}
```

### Fields

- `ok`
    - Type: `false`
    - Meaning: the command failed

- `command`
    - Type: literal string `"weather"`
    - Meaning: identifies the subcommand that produced this output

- `error`
    - Type: `str`
    - Meaning: human-readable error message
