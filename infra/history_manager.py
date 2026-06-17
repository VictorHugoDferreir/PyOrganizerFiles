import json
from pathlib import Path


class HistoryManager:

    HISTORY_FILE = "history.json"

    @classmethod
    def load_history(cls):

        path = Path(cls.HISTORY_FILE)

        if not path.exists():
            return []

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    @classmethod
    def save_history(cls, history):

        with open(
            cls.HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4,
                ensure_ascii=False
            )

    @classmethod
    def add_entry(cls, entry):

        history = cls.load_history()

        history.append(entry)

        cls.save_history(history)