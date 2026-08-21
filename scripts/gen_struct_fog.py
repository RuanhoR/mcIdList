#!/usr/bin/env python3
"""Generate JE translation JSON files for structures and fog categories."""
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BE_PATH = os.path.join(SCRIPT_DIR, "..", "data", "be_1.26.40.json")


def t(en, ja, ko, zh):
    return {"en": en, "ja": ja, "ko": ko, "zh": zh}


def read_be():
    with open(BE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def be_t(be_data, section, key):
    entry = be_data.get(section, {}).get(key)
    if entry:
        return {
            "en": entry.get("en", key),
            "ja": entry.get("ja", key),
            "ko": entry.get("ko", key),
            "zh": entry.get("zh", key),
        }
    return None


# ============================================================================
# STRUCTURES
# ============================================================================

JE_STRUCTURES = [
    "minecraft:ancient_city", "minecraft:bastion_remnant", "minecraft:buried_treasure",
    "minecraft:end_city", "minecraft:fortress", "minecraft:mansion",
    "minecraft:mineshaft", "minecraft:monument", "minecraft:pillager_outpost",
    "minecraft:ruined_portal", "minecraft:ruins", "minecraft:shipwreck",
    "minecraft:stronghold", "minecraft:temple", "minecraft:trail_ruins",
    "minecraft:trial_chambers", "minecraft:village", "minecraft:abandoned_camp",
]

STRUCTURE_JE_NAMES = {
    "minecraft:ancient_city": "Ancient City",
    "minecraft:bastion_remnant": "Bastion Remnant",
    "minecraft:buried_treasure": "Buried Treasure",
    "minecraft:end_city": "End City",
    "minecraft:fortress": "Nether Fortress",
    "minecraft:mansion": "Woodland Mansion",
    "minecraft:mineshaft": "Mineshaft",
    "minecraft:monument": "Ocean Monument",
    "minecraft:pillager_outpost": "Pillager Outpost",
    "minecraft:ruined_portal": "Ruined Portal",
    "minecraft:ruins": "Ocean Ruins",
    "minecraft:shipwreck": "Shipwreck",
    "minecraft:stronghold": "Stronghold",
    "minecraft:temple": "Desert Pyramid",
    "minecraft:trail_ruins": "Trail Ruins",
    "minecraft:trial_chambers": "Trial Chambers",
    "minecraft:village": "Village",
    "minecraft:abandoned_camp": "Abandoned Camp",
}

STRUCTURE_JE_EXCLUSIVE = {
    "minecraft:mansion": t("Woodland Mansion", "森の洋館", "숲의 저택", "林地府邸"),
    "minecraft:mineshaft": t("Mineshaft", "坑道", "광산", "废弃矿井"),
    "minecraft:monument": t("Ocean Monument", "海底神殿", "해저 신전", "海底神殿"),
    "minecraft:ruins": t("Ocean Ruins", "海底遺跡", "해저 유적", "海底遗迹"),
    "minecraft:temple": t("Desert Pyramid", "砂漠のピラミッド", "사막 피라미드", "沙漠神殿"),
    "minecraft:village": t("Village", "村", "마을", "村庄"),
}


# ============================================================================
# FOG
# ============================================================================

# Map of all 79 BE fog keys to their EN names and the BE biome translations.
# For fog entries, we read the BE biome data and append "Fog" suffix per language.
# BE fog keys use the Bedrock biome naming convention.

FOG_BE_MAP = {
    "minecraft:fog_bamboo_jungle": "minecraft:bamboo_jungle",
    "minecraft:fog_bamboo_jungle_hills": "minecraft:bamboo_jungle",
    "minecraft:fog_basalt_deltas": "minecraft:basalt_deltas",
    "minecraft:fog_beach": "minecraft:beach",
    "minecraft:fog_birch_forest": "minecraft:birch_forest",
    "minecraft:fog_birch_forest_hills": "minecraft:birch_forest",
    "minecraft:fog_cherry_grove": "minecraft:cherry_grove",
    "minecraft:fog_cold_beach": "minecraft:cold_beach",
    "minecraft:fog_cold_ocean": "minecraft:cold_ocean",
    "minecraft:fog_cold_taiga": "minecraft:cold_taiga",
    "minecraft:fog_cold_taiga_hills": "minecraft:cold_taiga",
    "minecraft:fog_cold_taiga_mutated": "minecraft:cold_taiga_mutated",
    "minecraft:fog_crimson_forest": "minecraft:crimson_forest",
    "minecraft:fog_deep_cold_ocean": "minecraft:deep_cold_ocean",
    "minecraft:fog_deep_frozen_ocean": "minecraft:deep_frozen_ocean",
    "minecraft:fog_deep_lukewarm_ocean": "minecraft:deep_lukewarm_ocean",
    "minecraft:fog_deep_ocean": "minecraft:deep_ocean",
    "minecraft:fog_deep_warm_ocean": "minecraft:deep_warm_ocean",
    "minecraft:fog_default": None,
    "minecraft:fog_desert": "minecraft:desert",
    "minecraft:fog_desert_hills": "minecraft:desert",
    "minecraft:fog_dry": None,
    "minecraft:fog_extreme_hills": "minecraft:extreme_hills",
    "minecraft:fog_extreme_hills_edge": "minecraft:extreme_hills",
    "minecraft:fog_extreme_hills_mutated": "minecraft:extreme_hills_mutated",
    "minecraft:fog_extreme_hills_plus_trees": "minecraft:extreme_hills_plus_trees",
    "minecraft:fog_extreme_hills_plus_trees_mutated": "minecraft:extreme_hills_plus_trees_mutated",
    "minecraft:fog_flower_forest": "minecraft:flower_forest",
    "minecraft:fog_forest": "minecraft:forest",
    "minecraft:fog_forest_hills": "minecraft:forest",
    "minecraft:fog_frozen_ocean": "minecraft:frozen_ocean",
    "minecraft:fog_frozen_river": "minecraft:frozen_river",
    "minecraft:fog_hell": "minecraft:hell",
    "minecraft:fog_humid": None,
    "minecraft:fog_ice_mountains": "minecraft:ice_plains",
    "minecraft:fog_ice_plains": "minecraft:ice_plains",
    "minecraft:fog_ice_plains_spikes": "minecraft:ice_plains_spikes",
    "minecraft:fog_jungle": "minecraft:jungle",
    "minecraft:fog_jungle_edge": "minecraft:jungle",
    "minecraft:fog_jungle_hills": "minecraft:jungle",
    "minecraft:fog_jungle_mutated": "minecraft:jungle_mutated",
    "minecraft:fog_lukewarm_ocean": "minecraft:lukewarm_ocean",
    "minecraft:fog_lush_caves": "minecraft:lush_caves",
    "minecraft:fog_mangrove_swamp": "minecraft:mangrove_swamp",
    "minecraft:fog_mega_spruce_taiga": "minecraft:mega_spruce_taiga",
    "minecraft:fog_mega_spruce_taiga_mutated": "minecraft:mega_spruce_taiga_mutated",
    "minecraft:fog_mega_taiga": "minecraft:mega_taiga",
    "minecraft:fog_mega_taiga_hills": "minecraft:mega_taiga",
    "minecraft:fog_mega_taiga_mutated": "minecraft:mega_taiga_mutated",
    "minecraft:fog_mesa": "minecraft:mesa",
    "minecraft:fog_mesa_bryce": "minecraft:mesa_bryce",
    "minecraft:fog_mesa_mutated": "minecraft:mesa_mutated",
    "minecraft:fog_mesa_plateau": "minecraft:mesa_plateau",
    "minecraft:fog_mesa_plateau_stone": "minecraft:mesa_plateau_stone",
    "minecraft:fog_mushroom_island": "minecraft:mushroom_island",
    "minecraft:fog_mushroom_island_shore": "minecraft:mushroom_island",
    "minecraft:fog_ocean": "minecraft:ocean",
    "minecraft:fog_pale_garden": "minecraft:pale_garden",
    "minecraft:fog_plains": "minecraft:plains",
    "minecraft:fog_powder_snow": None,
    "minecraft:fog_river": "minecraft:river",
    "minecraft:fog_roofed_forest": "minecraft:roofed_forest",
    "minecraft:fog_roofed_forest_mutated": "minecraft:roofed_forest",
    "minecraft:fog_savanna": "minecraft:savanna",
    "minecraft:fog_savanna_mutated": "minecraft:savanna_mutated",
    "minecraft:fog_savanna_plateau": "minecraft:savanna_plateau",
    "minecraft:fog_semi_humid": None,
    "minecraft:fog_soulsand_valley": "minecraft:soulsand_valley",
    "minecraft:fog_stone_beach": "minecraft:stone_beach",
    "minecraft:fog_sulfur_caves": "minecraft:sulfur_caves",
    "minecraft:fog_sunflower_plains": "minecraft:sunflower_plains",
    "minecraft:fog_swampland": "minecraft:swampland",
    "minecraft:fog_swampland_mutated": "minecraft:swampland",
    "minecraft:fog_taiga": "minecraft:taiga",
    "minecraft:fog_taiga_hills": "minecraft:taiga",
    "minecraft:fog_taiga_mutated": "minecraft:taiga_mutated",
    "minecraft:fog_the_end": "minecraft:the_end",
    "minecraft:fog_warm_ocean": "minecraft:warm_ocean",
    "minecraft:fog_warped_forest": "minecraft:warped_forest",
}

# EN names for all fog entries (79 total)
FOG_JE_NAMES = {
    "minecraft:fog_bamboo_jungle": "Bamboo Jungle Fog",
    "minecraft:fog_bamboo_jungle_hills": "Bamboo Jungle Hills Fog",
    "minecraft:fog_basalt_deltas": "Basalt Deltas Fog",
    "minecraft:fog_beach": "Beach Fog",
    "minecraft:fog_birch_forest": "Birch Forest Fog",
    "minecraft:fog_birch_forest_hills": "Birch Forest Hills Fog",
    "minecraft:fog_cherry_grove": "Cherry Grove Fog",
    "minecraft:fog_cold_beach": "Cold Beach Fog",
    "minecraft:fog_cold_ocean": "Cold Ocean Fog",
    "minecraft:fog_cold_taiga": "Cold Taiga Fog",
    "minecraft:fog_cold_taiga_hills": "Cold Taiga Hills Fog",
    "minecraft:fog_cold_taiga_mutated": "Snowy Taiga Fog",
    "minecraft:fog_crimson_forest": "Crimson Forest Fog",
    "minecraft:fog_deep_cold_ocean": "Deep Cold Ocean Fog",
    "minecraft:fog_deep_frozen_ocean": "Deep Frozen Ocean Fog",
    "minecraft:fog_deep_lukewarm_ocean": "Deep Lukewarm Ocean Fog",
    "minecraft:fog_deep_ocean": "Deep Ocean Fog",
    "minecraft:fog_deep_warm_ocean": "Deep Warm Ocean Fog",
    "minecraft:fog_default": "Default Fog",
    "minecraft:fog_desert": "Desert Fog",
    "minecraft:fog_desert_hills": "Desert Hills Fog",
    "minecraft:fog_dry": "Dry Fog",
    "minecraft:fog_extreme_hills": "Windswept Hills Fog",
    "minecraft:fog_extreme_hills_edge": "Windswept Hills Edge Fog",
    "minecraft:fog_extreme_hills_mutated": "Windswept Gravelly Hills Fog",
    "minecraft:fog_extreme_hills_plus_trees": "Windswept Forest Fog",
    "minecraft:fog_extreme_hills_plus_trees_mutated": "Windswept Forest Hills Fog",
    "minecraft:fog_flower_forest": "Flower Forest Fog",
    "minecraft:fog_forest": "Forest Fog",
    "minecraft:fog_forest_hills": "Forest Hills Fog",
    "minecraft:fog_frozen_ocean": "Frozen Ocean Fog",
    "minecraft:fog_frozen_river": "Frozen River Fog",
    "minecraft:fog_hell": "Nether Wastes Fog",
    "minecraft:fog_humid": "Humid Fog",
    "minecraft:fog_ice_mountains": "Ice Mountains Fog",
    "minecraft:fog_ice_plains": "Snowy Plains Fog",
    "minecraft:fog_ice_plains_spikes": "Ice Spikes Fog",
    "minecraft:fog_jungle": "Jungle Fog",
    "minecraft:fog_jungle_edge": "Jungle Edge Fog",
    "minecraft:fog_jungle_hills": "Jungle Hills Fog",
    "minecraft:fog_jungle_mutated": "Sparse Jungle Fog",
    "minecraft:fog_lukewarm_ocean": "Lukewarm Ocean Fog",
    "minecraft:fog_lush_caves": "Lush Caves Fog",
    "minecraft:fog_mangrove_swamp": "Mangrove Swamp Fog",
    "minecraft:fog_mega_spruce_taiga": "Giant Spruce Taiga Fog",
    "minecraft:fog_mega_spruce_taiga_mutated": "Modified Giant Spruce Taiga Fog",
    "minecraft:fog_mega_taiga": "Giant Tree Taiga Fog",
    "minecraft:fog_mega_taiga_hills": "Giant Tree Taiga Hills Fog",
    "minecraft:fog_mega_taiga_mutated": "Modified Giant Tree Taiga Fog",
    "minecraft:fog_mesa": "Badlands Fog",
    "minecraft:fog_mesa_bryce": "Eroded Badlands Fog",
    "minecraft:fog_mesa_mutated": "Modified Badlands Fog",
    "minecraft:fog_mesa_plateau": "Badlands Plateau Fog",
    "minecraft:fog_mesa_plateau_stone": "Wooded Badlands Fog",
    "minecraft:fog_mushroom_island": "Mushroom Island Fog",
    "minecraft:fog_mushroom_island_shore": "Mushroom Island Shore Fog",
    "minecraft:fog_ocean": "Ocean Fog",
    "minecraft:fog_pale_garden": "Pale Garden Fog",
    "minecraft:fog_plains": "Plains Fog",
    "minecraft:fog_powder_snow": "Powder Snow Fog",
    "minecraft:fog_river": "River Fog",
    "minecraft:fog_roofed_forest": "Dark Forest Fog",
    "minecraft:fog_roofed_forest_mutated": "Dark Forest Hills Fog",
    "minecraft:fog_savanna": "Savanna Fog",
    "minecraft:fog_savanna_mutated": "Windswept Savanna Fog",
    "minecraft:fog_savanna_plateau": "Savanna Plateau Fog",
    "minecraft:fog_semi_humid": "Semi-Humid Fog",
    "minecraft:fog_soulsand_valley": "Soul Sand Valley Fog",
    "minecraft:fog_stone_beach": "Stony Shore Fog",
    "minecraft:fog_sulfur_caves": "Sulfur Caves Fog",
    "minecraft:fog_sunflower_plains": "Sunflower Plains Fog",
    "minecraft:fog_swampland": "Swamp Fog",
    "minecraft:fog_swampland_mutated": "Swamp Hills Fog",
    "minecraft:fog_taiga": "Taiga Fog",
    "minecraft:fog_taiga_hills": "Taiga Hills Fog",
    "minecraft:fog_taiga_mutated": "Taiga Mountains Fog",
    "minecraft:fog_the_end": "The End Fog",
    "minecraft:fog_warm_ocean": "Warm Ocean Fog",
    "minecraft:fog_warped_forest": "Warped Forest Fog",
}


def add_fog_suffix(be_entry, lang):
    """Add fog suffix to biome name in the given language."""
    biome_name = be_entry[lang]
    if lang == "ja":
        return biome_name + "の霧"
    elif lang == "ko":
        return biome_name + " 안개"
    elif lang == "zh":
        return biome_name + "迷雾"
    return biome_name


FOG_JE_EXCLUSIVE = {
    "minecraft:fog_default": t("Default Fog", "デフォルトの霧", "기본 안개", "默认迷雾"),
    "minecraft:fog_dry": t("Dry Fog", "乾いた霧", "건조한 안개", "干燥迷雾"),
    "minecraft:fog_humid": t("Humid Fog", "湿った霧", "습한 안개", "潮湿迷雾"),
    "minecraft:fog_semi_humid": t("Semi-Humid Fog", "半湿った霧", "반습한 안개", "半潮湿迷雾"),
    "minecraft:fog_powder_snow": t("Powder Snow Fog", "粉雪の霧", "가루눈 안개", "细雪迷雾"),
    "minecraft:fog_deep_warm_ocean": t("Deep Warm Ocean Fog", "深い暖かい海の霧", "깊은 따뜻한 바다 안개", "暖水深海迷雾"),
    "minecraft:fog_mega_spruce_taiga": t("Giant Spruce Taiga Fog", "巨大トウヒのタイガの霧", "거대 소나무 타이가 안개", "巨型云杉针叶林迷雾"),
    "minecraft:fog_mega_spruce_taiga_mutated": t("Modified Giant Spruce Taiga Fog", "変種の巨大トウヒのタイガの霧", "변종 거대 소나무 타이가 안개", "变种巨型云杉针叶林迷雾"),
    "minecraft:fog_mega_taiga_mutated": t("Modified Giant Tree Taiga Fog", "変種の巨大樹のタイガの霧", "변종 거대 나무 타이가 안개", "变种巨型树木针叶林迷雾"),
    "minecraft:fog_mesa_mutated": t("Modified Badlands Fog", "変種のバッドランドの霧", "변종 메사 안개", "变种恶地迷雾"),
}


def make_fog_translations(be_data, fog_key):
    """Create fog translations for a given fog key using BE biome data."""
    # Check exclusive JE entries first
    if fog_key in FOG_JE_EXCLUSIVE:
        return FOG_JE_EXCLUSIVE[fog_key]

    biome_key = FOG_BE_MAP.get(fog_key)

    # If no biome mapping, use the fog key itself as biome reference
    if biome_key is None:
        en_name = FOG_JE_NAMES.get(fog_key, fog_key)
        return {
            "en": en_name,
            "ja": en_name,
            "ko": en_name,
            "zh": en_name,
        }

    en_name = FOG_JE_NAMES.get(fog_key)
    be_entry = be_t(be_data, "biome", biome_key)
    if be_entry is None:
        # Fallback: construct from fog key name
        fallback_name = fog_key.split(":")[-1].replace("fog_", "").replace("_", " ").title()
        return {
            "en": fallback_name + " Fog",
            "ja": fallback_name + "の霧",
            "ko": fallback_name + " 안개",
            "zh": fallback_name + "迷雾",
        }

    result = {"en": en_name}
    for lang in ["ja", "ko", "zh"]:
        result[lang] = add_fog_suffix(be_entry, lang)
    return result


# ============================================================================
# GENERATORS
# ============================================================================

def generate_structures(be_data):
    result = {}
    for je_key in JE_STRUCTURES:
        if je_key in STRUCTURE_JE_EXCLUSIVE:
            result[je_key] = STRUCTURE_JE_EXCLUSIVE[je_key]
        else:
            trans = be_t(be_data, "structure", je_key)
            if trans:
                en_name = STRUCTURE_JE_NAMES.get(je_key, trans["en"])
                result[je_key] = {
                    "en": en_name,
                    "ja": trans["ja"],
                    "ko": trans["ko"],
                    "zh": trans["zh"],
                }
            else:
                result[je_key] = {"en": je_key, "ja": je_key, "ko": je_key, "zh": je_key}
    return result


def generate_fogs(be_data):
    result = {}
    for fog_key in sorted(FOG_BE_MAP.keys()):
        trans = make_fog_translations(be_data, fog_key)
        if trans:
            result[fog_key] = trans
    return result


def write_json(data, filename):
    path = os.path.join(SCRIPT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  {filename}: {len(data)} entries")


def main():
    be_data = read_be()

    print("Generating JE translation files...")
    write_json(generate_structures(be_data), "je_structures.json")
    write_json(generate_fogs(be_data), "je_fogs.json")
    print("Done!")


if __name__ == "__main__":
    main()
