# MCIDList API

Minecraft data API. Provides queries and downloads for blocks, items, entities, and other data across platforms (BE/JE) and versions.

- `platform` values: `be` (Bedrock Edition), `je` (Java Edition)
- `version` format: `x.y.z` or `x.y.z.w` (e.g. `1.20.0`, `1.20.0.1`)
- `type` values (as defined in `mcidlist.ts` `allDataType`):

  | type | description |
  | --- | --- |
  | effect | status effects |
  | lootTable | loot tables |
  | item | items |
  | block | blocks |
  | entity | entities |
  | enchant | enchantments |
  | entityFamily | entity families |
  | entitySlot | entity equipment/slots |
  | biome | biomes |
  | structure | structures |
  | gamerule | game rules |
  | fog | fog definitions |
  | recipe | recipes |
  | particle | particles |
  | sound | sounds |
- Language fields: `zh`, `en`, `ko`, `ja` (plus `id`)

## API BASE

API BASE: `https://a.p.z.ruanhor.dpdns.org/`

## 1. Get Data by Type

`GET /mcidlist/:type/:version/:platform/json`

Returns a specific data category for a given platform and version.

### Path Parameters

| Param    | Type   | Description                            |
| -------- | ------ | -------------------------------------- |
| type     | string | Data type, must be in the allowed list |
| version  | string | Game version                           |
| platform | string | `be` or `je`                           |

### Success Response `200`

```json
{
  "code": 200,
  "success": true,
  "data": {
    "<key>": {
      "id": "minecraft:stone",
      "zh": "石头",
      "en": "Stone",
      "ko": "...",
      "ja": "..."
    }
  },
  "err": null
}
```

### Error Responses

| HTTP | code | err           | Description                |
| ---- | ---- | ------------- | -------------------------- |
| 400  | -1   | ERR_PARAM     | platform not in `[be, je]` |
| 400  | -1   | ERR_PARAM     | version format error       |
| 400  | -1   | ERR_PARAM     | type not in allowed list   |
| 404  | 404  | ERR_NOT_FOUND | Resource not found         |
| 500  | -1   | (message)     | Error while fetching data  |
| 500  | -1   | ERR_UNKOWN    | Unknown server error       |

---

## 2. Get Version List

`GET /mcidlist/:platform/version-list`

Returns the list of all available version numbers for a given platform.

### Path Parameters

| Param    | Type   | Description  |
| -------- | ------ | ------------ |
| platform | string | `be` or `je` |

### Success Response `200`

```json
{
  "code": 200,
  "success": true,
  "data": ["1.20.0", "1.20.1", "..."],
  "err": null
}
```

### Error Responses

| HTTP | code | err       | Description                |
| ---- | ---- | --------- | -------------------------- |
| 400  | -1   | ERR_PARAM | platform not in `[be, je]` |

---

## 3. Download Full Version Data

`GET /mcidlist/download/:platform/:version`

Downloads the full data (all categories) for a given platform and version.

### Path Parameters

| Param    | Type   | Description  |
| -------- | ------ | ------------ |
| platform | string | `be` or `je` |
| version  | string | Game version |

### Success Response `200`

```json
{
  "code": 200,
  "success": true,
  "data": {
    "effect": {},
    "lootTable": {},
    "item": {},
    "...": {}
  },
  "err": null
}
```

### Error Responses

| HTTP | code | err           | Description                |
| ---- | ---- | ------------- | -------------------------- |
| 400  | -1   | ERR_PARAM     | platform not in `[be, je]` |
| 400  | -1   | ERR_PARAM     | version format error       |
| 404  | 404  | ERR_NOT_FOUND | Resource not found         |
| 500  | -1   | (message)     | Error while fetching data  |
| 500  | -1   | ERR_UNKOWN    | Unknown server error       |

## Example

- Version Table: `https://a.p.z.ruanhor.dpdns.org/mcidlist/be/version-list` or `https://a.p.z.ruanhor.dpdns.org/mcidlist/je/version-list`
- Full Data For be 1.26.33.1: `https://a.p.z.ruanhor.dpdns.org/mcidlist/download/be/1.26.33.1`
- 1.26.33.1 Enchant data: `https://a.p.z.ruanhor.dpdns.org/mcidlist/enchant/1.26.33.1/be/json`
