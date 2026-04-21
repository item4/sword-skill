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

All commands must be run from the root directory of this skill project.

Invoke the CLI with `uv run`:

```shell
uv run sws <subcommand> ...
```

## Supported commands

### `weather`

This returns the latest real-time AWS observation data from Korea Meteorological Administration stations across South Korea.

#### Run Example

```shell
uv run sws weather
```

See `references/schema.md` for the output structure.

#### Output contract

The command prints a JSON object to stdout.

Common fields:
- `ok: bool` — whether the command succeeded
- `command: str` — command identifier

For `weather`, `command` is always `"weather"`.

When `ok` is `true`, the output also includes:

- `observed_at: str` — observation timestamp in ISO 8601 datetime format with timezone offset
- `records: list[Record]` — observation records from stations across South Korea

The detailed `Record` schema is documented in `references/schema.md`.

The `weather` command returns nationwide AWS observations across South Korea. It does not pre-filter records for a single place.
For location-specific use, first filter `records` by relevant fields such as `address` or station name before interpreting or summarizing the result.

If the schema is incomplete, treat `records` as structured station observation objects and inspect sample output before relying on individual fields.

#### Usage guidance

Use this skill when the user asks for current weather observation data in South Korea and structured nationwide AWS station measurements are useful.

If the user asks about a specific city, district, or area, do not treat the raw `records` list as a direct single-location answer. Filter the records first, then summarize the matching observations.

If the user only wants a short human-facing answer, summarize the filtered result instead of dumping raw JSON.

## Schema

If precise downstream parsing is needed, follow the schema in `references/schema.md`.
