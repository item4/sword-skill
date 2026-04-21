# Output Schema

## Common output rules

All commands must emit exactly one JSON object to stdout.

Common top-level fields:

- `ok: bool`
- `command: str`

`stderr` is reserved for logs or diagnostics and must not contain the primary result payload.

---

## `weather`

### Command

```shell
sws weather
```
### Success shape

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

### `Record` (WIP)

`Record` is not fully documented yet.

## Failure shape

WIP
