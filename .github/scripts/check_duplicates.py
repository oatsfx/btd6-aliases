import json
import glob
import sys
from collections import defaultdict

# Track if any duplicates are found across files.
found_duplicates = False

# Load all JSON files in aliases folder.
for file in glob.glob("../../aliases/*.json"):
    alias_map = defaultdict(list)

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        for game_object, aliases in data.items():
            for alias in aliases:
                alias_map[alias.lower()].append(game_object)

    # Find duplicates within this file.
    duplicates = {alias: objs for alias, objs in alias_map.items() if len(objs) > 1}

    if duplicates:
        found_duplicates = True
        print(f"❌ Duplicate aliases found in {file}:\n")
        for alias, objs in duplicates.items():
            print(f"  '{alias}' appears in:")
            for obj in objs:
                print(f"    - {obj}")
            print()

if found_duplicates:
    sys.exit(1)

print("✅ No duplicate aliases found in any file.")
