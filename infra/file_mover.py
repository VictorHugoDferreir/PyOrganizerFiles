# infra/file_mover.py

import shutil
from pathlib import Path


class FileMover:

    @staticmethod
    def resolve_conflict(dest_file):
        """
        arquivo.txt
        arquivo(1).txt
        arquivo(2).txt
        """

        dest_file = Path(dest_file)

        if not dest_file.exists():
            return dest_file

        counter = 1

        while True:

            new_name = (
                f"{dest_file.stem}({counter})"
                f"{dest_file.suffix}"
            )

            new_path = dest_file.parent / new_name

            if not new_path.exists():
                return new_path

            counter += 1

    @classmethod
    def move_file(cls, source, destination):

        source = Path(source)
        destination = Path(destination)

        destination.mkdir(
            parents=True,
            exist_ok=True
        )

        final_path = destination / source.name

        final_path = cls.resolve_conflict(final_path)

        shutil.move(
            str(source),
            str(final_path)
        )

        return final_path