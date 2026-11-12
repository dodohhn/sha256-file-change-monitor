import hashlib
from pathlib import Path
import json


script_folder = Path(__file__).resolve().parent
folder = script_folder / "data"
hash_file = script_folder / "hashes.json"


def hash_file_content(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


current = {}

for entry in folder.iterdir():
    if entry.is_file():
        current[entry.name] = hash_file_content(entry)


if hash_file.exists():
    with open(hash_file, "r", encoding = "utf-8") as f:
        old = json.load(f)
else:
    old = {}


for name, new_hash in current.items():
    if name not in old:
        print(f"Neu: {name}")
    elif old[name] != new_hash:
        print(f"Geändert: {name}")
    else:
        print(f"Unverändert: {name}")

for name in old:
    if name not in current:
        print(f"Gelöscht: {name}")

with open(hash_file, "w", encoding="utf-8") as f:
    json.dump(current, f, indent=2)