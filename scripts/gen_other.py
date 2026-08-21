#!/usr/bin/env python3
"""Generate JE translation JSON files for entities, biomes, effects, enchantments, particles, and gamerules."""
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


def snake_to_title(name):
    return name.replace("_", " ").title()


def make_trans(be_data, section, be_key, je_fallback, en_override=None):
    result = be_t(be_data, section, be_key)
    if result:
        if en_override:
            result["en"] = en_override
        return result
    title = en_override or snake_to_title(je_fallback)
    return {"en": title, "ja": title, "ko": title, "zh": title}


# ============================================================================
# ENTITIES
# ============================================================================

JE_ENTITIES = [
    "allay", "area_effect_cloud", "armor_stand", "arrow", "axolotl", "bat", "bee",
    "blaze", "breeze", "bogged", "camel", "camel_husk", "cat", "cave_spider",
    "chicken", "cod", "copper_golem", "cow", "creaking", "creeper", "dolphin",
    "donkey", "dragon_fireball", "drowned", "egg", "elder_guardian", "ender_crystal",
    "ender_dragon", "ender_pearl", "enderman", "endermite", "evoker", "evoker_fangs",
    "experience_bottle", "experience_orb", "eye_of_ender", "falling_block", "fireball",
    "firework_rocket", "fishing_bobber", "fox", "frog", "furnace_minecart", "ghast",
    "happy_ghast", "giant", "glow_item_frame", "glow_squid", "goat", "guardian",
    "hoglin", "hopper_minecart", "horse", "husk", "illusioner", "interaction",
    "iron_golem", "item", "item_display", "item_frame", "leash_knot", "lightning_bolt",
    "llama", "llama_spit", "magma_cube", "mannequin", "marker", "minecart", "mooshroom",
    "mule", "nautilus", "ocelot", "ominous_item_spawner", "painting", "panda", "parched",
    "parrot", "phantom", "pig", "piglin", "piglin_brute", "pillager", "polar_bear",
    "splash_potion", "lingering_potion", "pufferfish", "rabbit", "ravager", "salmon",
    "sheep", "shulker", "shulker_bullet", "silverfish", "skeleton", "skeleton_horse",
    "slime", "small_fireball", "sniffer", "snowball", "snow_golem", "spawner_minecart",
    "spectral_arrow", "spider", "squid", "stray", "strider", "sulfur_cube", "tadpole",
    "text_display", "tnt", "tnt_minecart", "trader_llama", "trident", "tropical_fish",
    "turtle", "vex", "villager", "vindicator", "wandering_trader", "warden",
    "wind_charge", "witch", "wither", "wither_skeleton", "wither_skull", "wolf",
    "zoglin", "zombie", "zombie_horse", "zombie_nautilus", "zombie_villager",
    "zombified_piglin", "player",
]

ENTITY_BE_MAP = {
    "evoker": "evocation_illager",
    "evoker_fangs": "evocation_fang",
    "experience_bottle": "xp_bottle",
    "experience_orb": "xp_orb",
    "eye_of_ender": "eye_of_ender_signal",
    "firework_rocket": "fireworks_rocket",
    "fishing_bobber": "fishing_hook",
    "trident": "thrown_trident",
    "tropical_fish": "tropicalfish",
    "zombified_piglin": "zombie_pigman",
    "lingering_potion": "lingering_potion",
    "splash_potion": "splash_potion",
}

ENTITY_JE_NAMES = {
    "evoker": "Evoker",
    "evoker_fangs": "Evoker Fangs",
    "experience_bottle": "Experience Bottle",
    "experience_orb": "Experience Orb",
    "eye_of_ender": "Eye of Ender",
    "firework_rocket": "Firework Rocket",
    "fishing_bobber": "Fishing Bobber",
    "trident": "Trident",
    "tropical_fish": "Tropical Fish",
    "zombified_piglin": "Zombified Piglin",
    "lingering_potion": "Lingering Potion",
    "splash_potion": "Splash Potion",
}

ENTITY_JE_EXCLUSIVE = {
    "giant": t("Giant", "ジャイアント", "자이언트", "巨人"),
    "glow_item_frame": t("Glow Item Frame", "発光額縁", "발광 액자", "发光物品展示框"),
    "illusioner": t("Illusioner", "イリュージョナー", "일루저너", "幻术师"),
    "interaction": t("Interaction", "インタラクション", "인터랙션", "交互实体"),
    "item_display": t("Item Display", "アイテムディスプレイ", "아이템 디스플레이", "物品展示"),
    "mannequin": t("Mannequin", "マネキン", "마네킹", "人体模型"),
    "marker": t("Marker", "マーカー", "마커", "标记"),
    "spectral_arrow": t("Spectral Arrow", "スペクトラルアロー", "신체 화살", "光灵箭"),
    "spawner_minecart": t("Spawner Minecart", "スポーンナー付き鉱車", "스포너 광산 수레", "刷怪笼矿车"),
    "text_display": t("Text Display", "テキストディスプレイ", "텍스트 디스플레이", "文本展示"),
    "wither_skull": t("Wither Skull", "ウィザーの頭蓋", "위더 두개골", "凋灵之首"),
}


# ============================================================================
# BIOMES
# ============================================================================

JE_BIOMES = [
    "the_void", "plains", "sunflower_plains", "snowy_plains", "ice_spikes", "desert",
    "swamp", "mangrove_swamp", "forest", "flower_forest", "birch_forest", "dark_forest",
    "pale_garden", "old_growth_birch_forest", "old_growth_pine_taiga",
    "old_growth_spruce_taiga", "taiga", "snowy_taiga", "savanna", "savanna_plateau",
    "windswept_hills", "windswept_gravelly_hills", "windswept_forest", "windswept_savanna",
    "jungle", "sparse_jungle", "bamboo_jungle", "badlands", "eroded_badlands",
    "wooded_badlands", "meadow", "cherry_grove", "grove", "snowy_slopes", "frozen_peaks",
    "jagged_peaks", "stony_peaks", "river", "frozen_river", "beach", "snowy_beach",
    "stony_shore", "warm_ocean", "lukewarm_ocean", "deep_lukewarm_ocean", "ocean",
    "deep_ocean", "cold_ocean", "deep_cold_ocean", "frozen_ocean", "deep_frozen_ocean",
    "mushroom_fields", "dripstone_caves", "lush_caves", "deep_dark", "sulfur_caves",
    "nether_wastes", "warped_forest", "crimson_forest", "soul_sand_valley",
    "basalt_deltas", "the_end", "end_highlands", "end_midlands", "small_end_islands",
    "end_barrens",
]

BIOME_BE_MAP = {
    "snowy_plains": "minecraft:ice_plains",
    "ice_spikes": "minecraft:ice_plains_spikes",
    "swamp": "minecraft:swampland",
    "dark_forest": "minecraft:roofed_forest",
    "old_growth_birch_forest": "minecraft:birch_forest_mutated",
    "old_growth_pine_taiga": "minecraft:mega_taiga",
    "old_growth_spruce_taiga": "minecraft:redwood_taiga_mutated",
    "snowy_taiga": "minecraft:cold_taiga",
    "windswept_hills": "minecraft:extreme_hills",
    "windswept_gravelly_hills": "minecraft:extreme_hills_mutated",
    "windswept_forest": "minecraft:extreme_hills_plus_trees",
    "windswept_savanna": "minecraft:savanna_mutated",
    "sparse_jungle": "minecraft:jungle_mutated",
    "badlands": "minecraft:mesa",
    "eroded_badlands": "minecraft:mesa_bryce",
    "wooded_badlands": "minecraft:mesa_plateau_stone",
    "snowy_beach": "minecraft:cold_beach",
    "stony_shore": "minecraft:stone_beach",
    "mushroom_fields": "minecraft:mushroom_island",
    "nether_wastes": "minecraft:hell",
    "soul_sand_valley": "minecraft:soulsand_valley",
    "plains": "minecraft:plains",
    "sunflower_plains": "minecraft:sunflower_plains",
    "desert": "minecraft:desert",
    "mangrove_swamp": "minecraft:mangrove_swamp",
    "forest": "minecraft:forest",
    "flower_forest": "minecraft:flower_forest",
    "birch_forest": "minecraft:birch_forest",
    "pale_garden": "minecraft:pale_garden",
    "taiga": "minecraft:taiga",
    "savanna": "minecraft:savanna",
    "savanna_plateau": "minecraft:savanna_plateau",
    "jungle": "minecraft:jungle",
    "bamboo_jungle": "minecraft:bamboo_jungle",
    "meadow": "minecraft:meadow",
    "cherry_grove": "minecraft:cherry_grove",
    "grove": "minecraft:grove",
    "snowy_slopes": "minecraft:snowy_slopes",
    "frozen_peaks": "minecraft:frozen_peaks",
    "jagged_peaks": "minecraft:jagged_peaks",
    "stony_peaks": "minecraft:stony_peaks",
    "river": "minecraft:river",
    "frozen_river": "minecraft:frozen_river",
    "beach": "minecraft:beach",
    "warm_ocean": "minecraft:warm_ocean",
    "lukewarm_ocean": "minecraft:lukewarm_ocean",
    "deep_lukewarm_ocean": "minecraft:deep_lukewarm_ocean",
    "ocean": "minecraft:ocean",
    "deep_ocean": "minecraft:deep_ocean",
    "cold_ocean": "minecraft:cold_ocean",
    "deep_cold_ocean": "minecraft:deep_cold_ocean",
    "frozen_ocean": "minecraft:frozen_ocean",
    "deep_frozen_ocean": "minecraft:deep_frozen_ocean",
    "dripstone_caves": "minecraft:dripstone_caves",
    "lush_caves": "minecraft:lush_caves",
    "deep_dark": "minecraft:deep_dark",
    "sulfur_caves": "minecraft:sulfur_caves",
    "warped_forest": "minecraft:warped_forest",
    "crimson_forest": "minecraft:crimson_forest",
    "basalt_deltas": "minecraft:basalt_deltas",
    "the_end": "minecraft:the_end",
}

BIOME_JE_EXCLUSIVE = {
    "the_void": t("The Void", "虚空", "공허", "虚空"),
    "end_highlands": t("End Highlands", "エンドハイランド", "엔드 고지", "末地高地"),
    "end_midlands": t("End Midlands", "エンドミッドランド", "엔드 중지", "末地中部"),
    "small_end_islands": t("Small End Islands", "小さなエンド島", "작은 엔드 섬", "末地小型岛屿"),
    "end_barrens": t("End Barrens", "エンド荒野", "엔드 황야", "末地荒芜之地"),
}

BIOME_JE_NAMES = {
    "snowy_plains": "Snowy Plains",
    "sparse_jungle": "Sparse Jungle",
    "wooded_badlands": "Wooded Badlands",
    "stony_shore": "Stony Shore",
    "nether_wastes": "Nether Wastes",
    "soul_sand_valley": "Soul Sand Valley",
}


# ============================================================================
# EFFECTS
# ============================================================================

JE_EFFECTS = [
    "speed", "slowness", "haste", "mining_fatigue", "strength", "instant_health",
    "instant_damage", "jump_boost", "nausea", "regeneration", "resistance",
    "fire_resistance", "water_breathing", "invisibility", "blindness", "night_vision",
    "hunger", "weakness", "poison", "wither", "health_boost", "absorption",
    "saturation", "glowing", "levitation", "luck", "unluck", "slow_falling",
    "conduit_power", "dolphins_grace", "bad_omen", "hero_of_the_village", "darkness",
    "trial_omen", "raid_omen", "wind_charged", "weaving", "oozing", "infested",
    "breath_of_the_nautilus",
]

EFFECT_BE_MAP = {
    "hero_of_the_village": "village_hero",
}

EFFECT_JE_NAMES = {
    "hero_of_the_village": "Hero of the Village",
    "mining_fatigue": "Mining Fatigue",
    "glowing": "Glowing",
    "luck": "Luck",
    "unluck": "Bad Luck",
    "dolphins_grace": "Dolphin's Grace",
}

EFFECT_JE_EXCLUSIVE = {
    "glowing": t("Glowing", "発光", "발광", "发光"),
    "luck": t("Luck", "幸運", "행운", "幸运"),
    "unluck": t("Bad Luck", "不運", "불행", "霉运"),
    "dolphins_grace": t("Dolphin's Grace", "イルカの恩恵", "돌고래의 은혜", "海豚的恩惠"),
    "mining_fatigue": t("Mining Fatigue", "採掘速度低下", "채굴 피로", "挖掘疲劳"),
}


# ============================================================================
# ENCHANTMENTS
# ============================================================================

JE_ENCHANTMENTS = [
    "protection", "fire_protection", "feather_falling", "blast_protection",
    "projectile_protection", "respiration", "aqua_affinity", "thorns", "depth_strider",
    "frost_walker", "binding_curse", "soul_speed", "swift_sneak", "sharpness", "smite",
    "bane_of_arthropods", "knockback", "fire_aspect", "looting", "sweeping_edge",
    "efficiency", "silk_touch", "unbreaking", "fortune", "power", "punch", "flame",
    "infinity", "luck_of_the_sea", "lure", "loyalty", "impaling", "riptide",
    "channeling", "multishot", "quick_charge", "piercing", "density", "breach",
    "wind_burst", "lunge", "mending", "vanishing_curse",
]

ENCHANT_NUMBER_IDS = {
    "protection": 0, "fire_protection": 1, "feather_falling": 2,
    "blast_protection": 3, "projectile_protection": 4, "thorns": 5,
    "respiration": 6, "aqua_affinity": 7, "depth_strider": 8, "sharpness": 9,
    "smite": 10, "bane_of_arthropods": 11, "knockback": 12, "fire_aspect": 13,
    "looting": 14, "sweeping_edge": 15, "efficiency": 16, "silk_touch": 17,
    "unbreaking": 18, "fortune": 19, "power": 20, "punch": 21, "flame": 22,
    "infinity": 23, "luck_of_the_sea": 24, "lure": 25, "frost_walker": 26,
    "mending": 27, "binding_curse": 28, "vanishing_curse": 29, "impaling": 30,
    "riptide": 31, "loyalty": 32, "channeling": 33, "multishot": 34,
    "quick_charge": 35, "piercing": 36, "soul_speed": 37, "swift_sneak": 38,
    "wind_burst": 39, "density": 40, "breach": 41, "lunge": 42,
}

ENCHANT_BE_MAP = {
    "binding_curse": "binding",
    "vanishing_curse": "vanishing",
}


# ============================================================================
# PARTICLES
# ============================================================================

JE_PARTICLES = [
    "ambient_entity_effect", "angry_villager", "block", "block_marker", "bubble",
    "bubble_column_up", "bubble_pop", "campfire_cosy_smoke", "campfire_signal_smoke",
    "cherry_leaves", "clamped_damage", "cloud", "composter", "crimson_spore", "crit",
    "damage_indicator", "dolphin", "dragon_breath", "dripping_honey", "dripping_lava",
    "dripping_obsidian_tear", "dripping_water", "dust_color_transition", "dust", "effect",
    "elder_guardian", "enchant", "enchanting_table", "end_rod", "entity_effect",
    "explosion_emitter", "explosion", "falling_dust", "falling_honey", "falling_lava",
    "falling_nectar", "falling_obsidian_tear", "falling_water", "firework", "fishing",
    "flame", "flash", "happy_villager", "heart", "infested", "item_slime",
    "item_snowball", "landing_honey", "landing_lava", "landing_obsidian_tear",
    "large_smoke", "lava", "mycelium", "nautilus", "note", "poof", "portal", "rain",
    "smoke", "sneeze", "snowflake", "sonic_boom", "soul", "soul_fire_flame", "spit",
    "squid_ink", "sweep_attack", "totem_of_undying", "trail", "trial_omen",
    "trial_spawner_detection", "underwater", "warped_spore", "weeping_vines",
    "white_smoke", "wind_charged", "pale_oak_leaves", "tinted_leaves",
]

PARTICLE_BE_MAP = {
    "ambient_entity_effect": "minecraft:mobspell_ambient",
    "angry_villager": "minecraft:villager_angry",
    "bubble": "minecraft:basic_bubble_particle",
    "bubble_column_up": "minecraft:bubble_column_up_particle",
    "campfire_cosy_smoke": "minecraft:campfire_smoke_particle",
    "campfire_signal_smoke": "minecraft:campfire_tall_smoke_particle",
    "cherry_leaves": "minecraft:cherry_leaves_particle",
    "crit": "minecraft:basic_crit_particle",
    "dolphin": "minecraft:dolphin_move_particle",
    "dragon_breath": "minecraft:dragon_breath_fire",
    "dripping_honey": "minecraft:honey_drip_particle",
    "dripping_lava": "minecraft:lava_drip_particle",
    "dripping_obsidian_tear": "minecraft:obsidian_tear_particle",
    "dripping_water": "minecraft:water_drip_particle",
    "effect": "minecraft:mobspell_emitter",
    "elder_guardian": "minecraft:guardian_attack_particle",
    "enchanting_table": "minecraft:enchanting_table_particle",
    "end_rod": "minecraft:endrod",
    "explosion_emitter": "minecraft:huge_explosion_emitter",
    "explosion": "minecraft:explosion_particle",
    "falling_dust": "minecraft:falling_dust",
    "falling_nectar": "minecraft:nectar_drip_particle",
    "fishing": "minecraft:fish_hook_particle",
    "flame": "minecraft:basic_flame_particle",
    "happy_villager": "minecraft:villager_happy",
    "heart": "minecraft:heart_particle",
    "infested": "minecraft:infested_ambient",
    "lava": "minecraft:lava_particle",
    "mycelium": "minecraft:mycelium_dust_particle",
    "nautilus": "minecraft:nautilus_bubbles_particle",
    "note": "minecraft:note_particle",
    "portal": "minecraft:basic_portal_particle",
    "rain": "minecraft:rain_splash_particle",
    "smoke": "minecraft:basic_smoke_particle",
    "sneeze": "minecraft:sneeze",
    "snowflake": "minecraft:snowflake_particle",
    "sonic_boom": "minecraft:sonic_explosion",
    "soul": "minecraft:soul_particle",
    "soul_fire_flame": "minecraft:small_soul_fire_flame",
    "spit": "minecraft:llama_spit_smoke",
    "squid_ink": "minecraft:squid_ink_bubble",
    "totem_of_undying": "minecraft:totem_particle",
    "trial_omen": "minecraft:trial_omen_ambient",
    "trial_spawner_detection": "minecraft:trial_spawner_detection",
    "underwater": "minecraft:underwater_torch_particle",
    "white_smoke": "minecraft:white_smoke_particle",
    "wind_charged": "minecraft:wind_charged_ambient",
    "pale_oak_leaves": "minecraft:pale_oak_leaves_particle",
    "tinted_leaves": "minecraft:biome_tinted_leaves_particle",
}


# ============================================================================
# GAMERULES
# ============================================================================

JE_GAMERULES = [
    "advancetime", "commandblockoutput", "commandblocksenabled", "dodaylightcycle",
    "doentitydrops", "dofiretick", "doimmediaterespawn", "doinsomnia",
    "dolimitedcrafting", "domobloot", "domobspawning", "dotiledrops",
    "doweathercycle", "drowningdamage", "falldamage", "firedamage", "freezedamage",
    "functioncommandlimit", "keepinventory", "maxcommandchainlength", "mobgriefing",
    "naturalregeneration", "playersleepingpercentage", "pvp", "randomtickspeed",
    "sendcommandfeedback", "spawnradius", "tntexplodes",
]

GAMERULE_BE_MAP = {}

GAMERULE_JE_EXCLUSIVE = {
    "advancetime": t("Advance Time", "時刻を進める", "시간 진행", "推进时间"),
}


# ============================================================================
# GENERATORS
# ============================================================================

def generate_entities(be_data):
    result = {}
    for je_key in JE_ENTITIES:
        be_key = ENTITY_BE_MAP.get(je_key, je_key)
        en_override = ENTITY_JE_NAMES.get(je_key)
        if je_key in ENTITY_JE_EXCLUSIVE:
            result[je_key] = ENTITY_JE_EXCLUSIVE[je_key]
        else:
            result[je_key] = make_trans(be_data, "entity", be_key, je_key, en_override=en_override)
    return result


def generate_biomes(be_data):
    result = {}
    for je_key in JE_BIOMES:
        be_key = BIOME_BE_MAP.get(je_key, f"minecraft:{je_key}")
        en_override = BIOME_JE_NAMES.get(je_key)
        if je_key in BIOME_JE_EXCLUSIVE:
            result[je_key] = BIOME_JE_EXCLUSIVE[je_key]
        else:
            result[je_key] = make_trans(be_data, "biome", be_key, je_key, en_override=en_override)
    return result


def generate_effects(be_data):
    result = {}
    for je_key in JE_EFFECTS:
        be_key = EFFECT_BE_MAP.get(je_key, je_key)
        en_override = EFFECT_JE_NAMES.get(je_key)
        if je_key in EFFECT_JE_EXCLUSIVE:
            result[je_key] = EFFECT_JE_EXCLUSIVE[je_key]
        else:
            result[je_key] = make_trans(be_data, "effect", be_key, je_key, en_override=en_override)
    return result


def generate_enchantments(be_data):
    result = {}
    for je_key in JE_ENCHANTMENTS:
        be_key = ENCHANT_BE_MAP.get(je_key, je_key)
        trans = make_trans(be_data, "enchant", be_key, je_key)
        result[je_key] = {"numberId": ENCHANT_NUMBER_IDS[je_key], **trans}
    return result


PARTICLE_JE_NAMES = {
    "ambient_entity_effect": "Ambient Entity Effect",
    "angry_villager": "Angry Villager",
    "bubble": "Bubble",
    "bubble_column_up": "Bubble Column Up",
    "campfire_cosy_smoke": "Campfire Cosy Smoke",
    "campfire_signal_smoke": "Campfire Signal Smoke",
    "cherry_leaves": "Cherry Leaves",
    "crit": "Crit",
    "dolphin": "Dolphin",
    "dragon_breath": "Dragon's Breath",
    "dripping_honey": "Dripping Honey",
    "dripping_lava": "Dripping Lava",
    "dripping_obsidian_tear": "Dripping Obsidian Tear",
    "dripping_water": "Dripping Water",
    "effect": "Effect",
    "elder_guardian": "Elder Guardian",
    "enchanting_table": "Enchanting Table",
    "end_rod": "End Rod",
    "explosion_emitter": "Explosion Emitter",
    "explosion": "Explosion",
    "falling_dust": "Falling Dust",
    "falling_nectar": "Falling Nectar",
    "fishing": "Fishing",
    "flame": "Flame",
    "happy_villager": "Happy Villager",
    "heart": "Heart",
    "infested": "Infested",
    "lava": "Lava",
    "mycelium": "Mycelium",
    "nautilus": "Nautilus",
    "note": "Note",
    "portal": "Portal",
    "rain": "Rain",
    "smoke": "Smoke",
    "sneeze": "Sneeze",
    "snowflake": "Snowflake",
    "sonic_boom": "Sonic Boom",
    "soul": "Soul",
    "soul_fire_flame": "Soul Fire Flame",
    "spit": "Spit",
    "squid_ink": "Squid Ink",
    "totem_of_undying": "Totem of Undying",
    "trial_omen": "Trial Omen",
    "trial_spawner_detection": "Trial Spawner Detection",
    "underwater": "Underwater",
    "white_smoke": "White Smoke",
    "wind_charged": "Wind Charged",
    "pale_oak_leaves": "Pale Oak Leaves",
    "tinted_leaves": "Tinted Leaves",
}


def generate_particles(be_data):
    result = {}
    for je_key in JE_PARTICLES:
        be_key = PARTICLE_BE_MAP.get(je_key)
        en_name = PARTICLE_JE_NAMES.get(je_key, snake_to_title(je_key))
        if be_key:
            result[je_key] = make_trans(be_data, "particle", be_key, je_key, en_override=en_name)
        else:
            result[je_key] = {"en": en_name, "ja": en_name, "ko": en_name, "zh": en_name}
    return result


def generate_gamerules(be_data):
    result = {}
    for je_key in JE_GAMERULES:
        if je_key in GAMERULE_JE_EXCLUSIVE:
            result[je_key] = GAMERULE_JE_EXCLUSIVE[je_key]
        else:
            be_key = GAMERULE_BE_MAP.get(je_key, je_key)
            result[je_key] = make_trans(be_data, "gamerule", be_key, je_key)
    return result


def write_json(data, filename):
    path = os.path.join(SCRIPT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  {filename}: {len(data)} entries")


def main():
    be_data = read_be()

    print("Generating JE translation files...")
    write_json(generate_entities(be_data), "je_entities.json")
    write_json(generate_biomes(be_data), "je_biomes.json")
    write_json(generate_effects(be_data), "je_effects.json")
    write_json(generate_enchantments(be_data), "je_enchantments.json")
    write_json(generate_particles(be_data), "je_particles.json")
    write_json(generate_gamerules(be_data), "je_gamerules.json")
    print("Done!")


if __name__ == "__main__":
    main()
