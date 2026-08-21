#!/usr/bin/env python3
import json, os

scripts_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(os.path.dirname(scripts_dir), 'data')

def load_json(filename):
    path = os.path.join(scripts_dir, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

items = load_json('je_items.json')
blocks = load_json('je_blocks.json')
entities = load_json('je_entities.json')
biomes = load_json('je_biomes.json')
effects = load_json('je_effects.json')
enchantments = load_json('je_enchantments.json')
particles = load_json('je_particles.json')
gamerules = load_json('je_gamerules.json')
sounds = load_json('je_sounds.json')
loottables = load_json('je_loottables.json')
entityfamilies = load_json('je_entityfamilies.json')
entityslots = load_json('je_entityslots.json')
structures = load_json('je_structures.json')
fogs = load_json('je_fogs.json')
recipes = load_json('je_recipes.json')

data = {
    'item': items,
    'block': blocks,
    'entity': entities,
    'effect': effects,
    'enchant': enchantments,
    'biome': biomes,
    'particle': particles,
    'gamerule': gamerules,
    'sound': sounds,
    'lootTable': loottables,
    'entityFamily': entityfamilies,
    'entitySlot': entityslots,
    'structure': structures,
    'fog': fogs,
    'recipe': recipes
}

output_path = os.path.join(data_dir, 'je_1.26.2.json')
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Generated {output_path}')
for k, v in data.items():
    print(f'  {k}: {len(v)} entries')
size = os.path.getsize(output_path)
print(f'File size: {size:,} bytes ({size/1024:.1f} KB)')
