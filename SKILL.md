---
name: sword-skill
description: Query structured utility data through the `sws` CLI. Currently supports real-time Korea Meteorological Administration AWS weather observations across South Korea. Use when the user asks for current South Korea weather observations or nationwide station data.
---

# Sword Skill

Use this skill to retrieve structured data from the local `sws` CLI.

## Installation and Update

If dependencies are not installed yet, run:

```shell
uv sync
```

## Command entrypoint

All commands are invoked through:

```shell
sws <subcommand> ...
```

## Supported commands

### `weather`

This returns the latest real-time AWS observation data from Korea Meteorological Administration stations across South Korea.

#### Run

```shell
sws weather
```

#### Output contract

The command prints a JSON object to stdout.

Common fields:
- `ok: bool` — whether the command succeeded
- `command: str` — command identifier

For `weather`, `command` is always `"weather"`.

When `ok` is `true`, the output also includes:

- `observed_at: str` — observation timestamp in ISO 8601 datetime format with timezone offset
- `records: list[Record]` — observation records from stations across South Korea

The detailed `Record` schema is documented in `references/schema.md`. If that schema is incomplete, treat `records` as structured station observation objects and inspect sample output before relying on individual fields.

#### Usage guidance

Use this skill when the user asks for current weather observation data in South Korea and structured nationwide AWS station measurements are useful.

If the user only wants a short human-facing answer, summarize the returned JSON instead of dumping raw output.

## Schema

If precise downstream parsing is needed, follow the schema in `references/schema.md`.
