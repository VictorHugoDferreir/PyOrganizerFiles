# infra/config_loader.py

import json
from pathlib import Path


class ConfigLoader:

    CONFIG_FILE = "config.json"

    @classmethod
    def load_config(cls):
        path = Path(cls.CONFIG_FILE)

        if not path.exists():
            return {
                "default_destination": ""
            }

        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    @classmethod
    def save_config(cls, config):
        with open(cls.CONFIG_FILE, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4)

    @classmethod
    def get_default_dest(cls):
        config = cls.load_config()
        return config.get("default_destination", "")