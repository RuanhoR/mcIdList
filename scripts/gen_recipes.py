#!/usr/bin/env python3
"""Generate JE recipes JSON by copying BE recipe translations."""
import json
import os

def main():
    be_path = os.path.join(os.path.dirname(__file__), "..", "data", "be_1.26.40.json")
    with open(be_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    recipes = data.get("recipe", {})

    out_path = os.path.join(os.path.dirname(__file__), "je_recipes.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(recipes, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(recipes)} recipes -> {out_path}")

if __name__ == "__main__":
    main()
