# MCIDLIST

> RuanhoR's mc id repo.

## How to use?

1. Just trying it out
   Go [My Tool Website](https://ruanhor.dpdns.org/tool) and click `MCID List`(The website support i18n, so also call `MCID 列表` or `MCID リスト`) and use the tool

2. Use on your app
   Have three methods

- Use `./data` assets(type see `DataType`)
- Use the API in ./docs/api.md
- Download from [Be](https://npmjs.com/package/@ojaang/be-vanilla-iddata) or `je (No data)`

## DataType

#### TS Example

```typescript
const allDataType = [
  "effect",
  "lootTable",
  "item",
  "block",
  "entity",
  "enchant",
  "entityFamily",
  "entitySlot",
  "biome",
  "structure",
  "gamerule",
  "fog",
  "recipe",
  "particle",
  "sound",
] as const;
const allLanguage = ["zh", "en", "ko", "ja"] as const;
type DataValueMapping = {
  [key in (typeof allLanguage)[number] | "id"]: string;
};
type allPlatform = "be" | "je";
interface DataValue extends DataValueMapping {
  numberId?: number;
}
type VersionData = {
  [key in (typeof allDataType)[number]]: {
    [key in string]: DataValue;
  };
};
```
