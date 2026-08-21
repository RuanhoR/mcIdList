#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator script for JE blocks translations."""
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BE_FILE = os.path.join(SCRIPT_DIR, '..', 'data', 'be_1.26.40.json')
NAMES_FILE = os.path.join(SCRIPT_DIR, 'je_block_names.json')
MANUAL_FILE = os.path.join(SCRIPT_DIR, 'je_manual.json')
OUTPUT_FILE = os.path.join(SCRIPT_DIR, 'je_blocks.json')

def main():
    with open(NAMES_FILE, 'r', encoding='utf-8') as f:
        je_block_names = json.load(f)

    with open(MANUAL_FILE, 'r', encoding='utf-8') as f:
        je_manual = json.load(f)

    d = json.load(open(BE_FILE, 'r', encoding='utf-8'))
    be_blocks = d['block']

    result = {}
    missing = []
    for name in je_block_names:
        if name in be_blocks:
            result[name] = be_blocks[name]
        elif name in je_manual:
            result[name] = je_manual[name]
        else:
            missing.append(name)
            result[name] = {
                'en': name.replace('_', ' ').title(),
                'ja': name,
                'ko': name,
                'zh': name
            }

    if missing:
        print(f'WARNING: Missing manual translations for {len(missing)} blocks:', file=sys.stderr)
        for m in missing:
            print(f'  {m}', file=sys.stderr)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f'Generated {OUTPUT_FILE} with {len(result)} blocks')

if __name__ == '__main__':
    main()
