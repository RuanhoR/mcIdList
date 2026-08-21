#!/usr/bin/env python3
"""Generate JE translation JSON files for loot tables, entity families, and entity slots."""
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BE_PATH = os.path.join(SCRIPT_DIR, "..", "data", "be_1.26.40.json")


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
# LOOT TABLES (207 entries)
# ============================================================================

JE_LOOTTABLES = [
    "chests/abandoned_mineshaft",
    "chests/ancient_city",
    "chests/ancient_city_ice_box",
    "chests/bastion_bridge",
    "chests/bastion_hoglin_stable",
    "chests/bastion_other",
    "chests/bastion_treasure",
    "chests/buriedtreasure",
    "chests/desert_pyramid",
    "chests/dispenser_trap",
    "chests/end_city_treasure",
    "chests/igloo_chest",
    "chests/jungle_temple",
    "chests/monster_room",
    "chests/nether_bridge",
    "chests/pillager_outpost",
    "chests/ruined_portal",
    "chests/shipwreck",
    "chests/shipwrecksupply",
    "chests/shipwrecktreasure",
    "chests/simple_dungeon",
    "chests/spawn_bonus_chest",
    "chests/stronghold_corridor",
    "chests/stronghold_crossing",
    "chests/stronghold_library",
    "chests/trial_chambers/corridor",
    "chests/trial_chambers/entrance",
    "chests/trial_chambers/intersection",
    "chests/trial_chambers/intersection_barrel",
    "chests/trial_chambers/reward",
    "chests/trial_chambers/reward_common",
    "chests/trial_chambers/reward_ominous",
    "chests/trial_chambers/reward_ominous_common",
    "chests/trial_chambers/reward_ominous_rare",
    "chests/trial_chambers/reward_ominous_unique",
    "chests/trial_chambers/reward_rare",
    "chests/trial_chambers/reward_unique",
    "chests/trial_chambers/supply",
    "chests/underwater_ruin_big",
    "chests/underwater_ruin_small",
    "chests/village/village_armorer",
    "chests/village/village_bundle",
    "chests/village/village_butcher",
    "chests/village/village_cartographer",
    "chests/village/village_desert_house",
    "chests/village/village_fletcher",
    "chests/village/village_mason",
    "chests/village/village_plains_house",
    "chests/village/village_savanna_house",
    "chests/village/village_shepherd",
    "chests/village/village_snowy_house",
    "chests/village/village_taiga_house",
    "chests/village/village_tannery",
    "chests/village/village_temple",
    "chests/village/village_toolsmith",
    "chests/village/village_weaponsmith",
    "chests/village_blacksmith",
    "chests/village_two_room_house",
    "chests/woodland_mansion",
    "dispensers/trial_chambers/chamber",
    "dispensers/trial_chambers/corridor",
    "dispensers/trial_chambers/water",
    "empty",
    "entities/armadillo_brush",
    "entities/armor_set_chain",
    "entities/armor_set_copper",
    "entities/armor_set_diamond",
    "entities/armor_set_gold",
    "entities/armor_set_iron",
    "entities/armor_set_leather",
    "entities/armor_stand",
    "entities/bat",
    "entities/blaze",
    "entities/boat",
    "entities/bogged",
    "entities/bogged_shear",
    "entities/breeze",
    "entities/brown_mooshroom_shear",
    "entities/camel_husk",
    "entities/cat",
    "entities/cat_gift",
    "entities/cave_spider",
    "entities/chicken",
    "entities/clownfish",
    "entities/cold_ocean_ruins_brushable_block",
    "entities/copper_golem",
    "entities/copper_golem_shear",
    "entities/cow",
    "entities/creeper",
    "entities/desert_pyramid_brushable_block",
    "entities/desert_well_brushable_block",
    "entities/dolphin",
    "entities/drowned",
    "entities/drowned_equipment",
    "entities/drowned_ranged_equipment",
    "entities/drowned_rider_equipment",
    "entities/elder_guardian",
    "entities/empty_brushable_block",
    "entities/enderman",
    "entities/endermite",
    "entities/evocation_illager",
    "entities/fish",
    "entities/fox_equipment",
    "entities/frog",
    "entities/ghast",
    "entities/giant",
    "entities/glow_squid",
    "entities/goat",
    "entities/guardian",
    "entities/hoglin",
    "entities/horse",
    "entities/husk_rider",
    "entities/iron_golem",
    "entities/llama",
    "entities/magma_cube",
    "entities/mooshroom",
    "entities/mooshroom_shear",
    "entities/nautilus",
    "entities/ocelot",
    "entities/panda",
    "entities/panda_sneeze",
    "entities/parched",
    "entities/parrot",
    "entities/phantom",
    "entities/pig",
    "entities/pig_saddled",
    "entities/piglin_barter",
    "entities/piglin_brute_gear",
    "entities/piglin_gear_melee",
    "entities/piglin_gear_ranged",
    "entities/pillager",
    "entities/pillager_captain",
    "entities/pillager_captain_equipment",
    "entities/pillager_gear",
    "entities/pillager_raid",
    "entities/polar_bear",
    "entities/pufferfish",
    "entities/rabbit",
    "entities/raider_drops",
    "entities/ravager",
    "entities/saddle",
    "entities/salmon_large",
    "entities/salmon_normal",
    "entities/sea_turtle",
    "entities/sheep",
    "entities/sheep_shear",
    "entities/sheep_sheared",
    "entities/shulker",
    "entities/silverfish",
    "entities/skeleton",
    "entities/skeleton_gear",
    "entities/skeleton_horse",
    "entities/slime",
    "entities/snow_golem_shear",
    "entities/snowman",
    "entities/spider",
    "entities/squid",
    "entities/stray",
    "entities/strider",
    "entities/strider_saddled",
    "entities/trail_ruins_brushable_block_common",
    "entities/trail_ruins_brushable_block_rare",
    "entities/tropicalfish",
    "entities/vex_gear",
    "entities/vindication_illager",
    "entities/vindicator_captain_equipment",
    "entities/vindicator_gear",
    "entities/vindicator_raid",
    "entities/warden",
    "entities/warm_ocean_ruins_brushable_block",
    "entities/witch",
    "entities/wither_boss",
    "entities/wither_skeleton",
    "entities/wither_skeleton_gear",
    "entities/wolf",
    "entities/zoglin",
    "entities/zombie",
    "entities/zombie_equipment",
    "entities/zombie_horse",
    "entities/zombie_nautilus",
    "entities/zombie_pigman",
    "entities/zombie_pigman_gear",
    "entities/zombie_rider",
    "entities/zombie_rider_equipment",
    "entities/zombified_piglin_rider_gear",
    "equipment/low_tier_items",
    "equipment/trial_chamber",
    "equipment/trial_chamber_chainmail",
    "equipment/trial_chamber_diamond",
    "equipment/trial_chamber_iron",
    "equipment/trial_chamber_melee",
    "equipment/trial_chamber_ranged",
    "gameplay/entities/mooshroom_milking",
    "gameplay/entities/sniffer_seeds",
    "gameplay/fishing",
    "gameplay/fishing/fish",
    "gameplay/fishing/jungle_fish",
    "gameplay/fishing/jungle_junk",
    "gameplay/fishing/junk",
    "gameplay/fishing/treasure",
    "gameplay/jungle_fishing",
    "pots/trial_chambers/corridor",
    "spawners/ominous/trial_chamber/consumables",
    "spawners/ominous/trial_chamber/key",
    "spawners/trial_chamber/consumables",
    "spawners/trial_chamber/items_to_drop_when_ominous",
    "spawners/trial_chamber/key",
]


def generate_loottables(be_data):
    result = {}
    for key in JE_LOOTTABLES:
        trans = be_t(be_data, "lootTable", key)
        if trans:
            result[key] = trans
        else:
            name = key.split("/")[-1].replace("_", " ").title()
            result[key] = {"en": name, "ja": name, "ko": name, "zh": name}
    return result


# ============================================================================
# ENTITY FAMILIES (147 entries)
# ============================================================================

# JE uses different English names for some entity families
EF_JE_NAMES = {
    "baby_zombie_pigman": "Baby Zombified Piglin",
    "blacksmith": "Blacksmith",
    "dragon": "Ender Dragon",
    "evocation_illager": "Evoker",
    "guardian_elder": "Elder Guardian",
    "hoglin_huntable": "Huntable Hoglin",
    "irongolem": "Iron Golem",
    "magmacube": "Magma Cube",
    "mushroomcow": "Mooshroom",
    "skeletonhorse": "Skeleton Horse",
    "snowgolem": "Snow Golem",
    "zombiehorse": "Zombie Horse",
}

EF_JE_EXCLUSIVE = {}


def generate_entityfamilies(be_data):
    result = {}
    for key, val in be_data.get("entityFamily", {}).items():
        if key in EF_JE_EXCLUSIVE:
            result[key] = EF_JE_EXCLUSIVE[key]
        else:
            trans = {
                "en": val.get("en", key),
                "ja": val.get("ja", key),
                "ko": val.get("ko", key),
                "zh": val.get("zh", key),
            }
            en_override = EF_JE_NAMES.get(key)
            if en_override:
                trans["en"] = en_override
            result[key] = trans
    for key, val in EF_JE_EXCLUSIVE.items():
        if key not in result:
            result[key] = val
    return result


# ============================================================================
# ENTITY SLOTS (14 entries)
# ============================================================================

JE_ENTITYSLOTS = [
    "slot.armor",
    "slot.armor.body",
    "slot.armor.chest",
    "slot.armor.feet",
    "slot.armor.head",
    "slot.armor.legs",
    "slot.chest",
    "slot.enderchest",
    "slot.equippable",
    "slot.hotbar",
    "slot.inventory",
    "slot.saddle",
    "slot.weapon.mainhand",
    "slot.weapon.offhand",
]

ES_JE_NAMES = {
    "slot.armor": "Armor Slot",
    "slot.armor.body": "Body Armor",
    "slot.armor.chest": "Chestplate",
    "slot.armor.feet": "Boots",
    "slot.armor.head": "Helmet",
    "slot.armor.legs": "Leggings",
    "slot.chest": "Container",
    "slot.enderchest": "Ender Chest Inventory",
    "slot.equippable": "Equippable",
    "slot.hotbar": "Hotbar",
    "slot.inventory": "Inventory",
    "slot.saddle": "Saddle",
    "slot.weapon.mainhand": "Mainhand",
    "slot.weapon.offhand": "Offhand",
}

ES_JE_ZH = {
    "slot.armor": "盔甲槽位",
    "slot.armor.body": "身体护甲",
    "slot.armor.chest": "胸甲",
    "slot.armor.feet": "靴子",
    "slot.armor.head": "头盔",
    "slot.armor.legs": "护腿",
    "slot.chest": "容器",
    "slot.enderchest": "末影箱物品栏",
    "slot.equippable": "可装备",
    "slot.hotbar": "快捷栏",
    "slot.inventory": "物品栏",
    "slot.saddle": "鞍",
    "slot.weapon.mainhand": "主手",
    "slot.weapon.offhand": "副手",
}

ES_JE_JA = {
    "slot.armor": "防具スロット",
    "slot.armor.body": "ボディアーマー",
    "slot.armor.chest": "チェストプレート",
    "slot.armor.feet": "ブーツ",
    "slot.armor.head": "ヘルメット",
    "slot.armor.legs": "レギンス",
    "slot.chest": "コンテナ",
    "slot.enderchest": "エンダーチェストのインベントリ",
    "slot.equippable": "装備可能",
    "slot.hotbar": "ホットバー",
    "slot.inventory": "インベントリ",
    "slot.saddle": "鞍",
    "slot.weapon.mainhand": "メインハンド",
    "slot.weapon.offhand": "オフハンド",
}

ES_JE_KO = {
    "slot.armor": "갑옷 슬롯",
    "slot.armor.body": "바디 아머",
    "slot.armor.chest": "흉갑",
    "slot.armor.feet": "부츠",
    "slot.armor.head": "투구",
    "slot.armor.legs": "레깅스",
    "slot.chest": "컨테이너",
    "slot.enderchest": "엔더 상자 인벤토리",
    "slot.equippable": "장착 가능",
    "slot.hotbar": "단축바",
    "slot.inventory": "인벤토리",
    "slot.saddle": "안장",
    "slot.weapon.mainhand": "주손",
    "slot.weapon.offhand": "보조손",
}


def generate_entityslots(be_data):
    result = {}
    for key in JE_ENTITYSLOTS:
        result[key] = {
            "en": ES_JE_NAMES.get(key, key),
            "ja": ES_JE_JA.get(key, key),
            "ko": ES_JE_KO.get(key, key),
            "zh": ES_JE_ZH.get(key, key),
        }
    return result


# ============================================================================
# GENERATORS
# ============================================================================

def write_json(data, filename):
    path = os.path.join(SCRIPT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  {filename}: {len(data)} entries")


def main():
    be_data = read_be()

    print("Generating JE translation files...")
    write_json(generate_loottables(be_data), "je_loottables.json")
    write_json(generate_entityfamilies(be_data), "je_entityfamilies.json")
    write_json(generate_entityslots(be_data), "je_entityslots.json")
    print("Done!")


if __name__ == "__main__":
    main()
