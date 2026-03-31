import json
import os

class Storage:
    FILE = "characters.json"

    @staticmethod
    def save(data):
        with open(Storage.FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def load():
        if not os.path.exists(Storage.FILE):
            return []

        with open(Storage.FILE, "r", encoding="utf-8") as f:
            return json.load(f)
