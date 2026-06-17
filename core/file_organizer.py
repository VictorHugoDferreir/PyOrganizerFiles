# Classe principal que orquestra a organização de arquivos

from importlib.resources import files
from pathlib import Path
from infra.file_mover import FileMover
from core.file_classifier import FileClassifier
from infra.history_manager import HistoryManager

class FileOrganizer:

    def __init__(self, logger):

        self.logger = logger

        self.last_run = []

    def run(
        self,
        source_folder,
        destination_folder,
        progress_callback=None
    ):

        source_path = Path(source_folder)

        if not source_path.exists():
            raise FileNotFoundError(
                f"Pasta não encontrada: {source_folder}"
            )

        files = [
            f for f in source_path.iterdir()
            if f.is_file()
        ]

        if not files:
            self.logger.warning("Nenhum arquivo encontrado.")
            return {
                "total": 0,
                "Imagens": 0,
                "Documentos": 0,
                "Videos": 0,
                "Compactados": 0,
                "Outros": 0
            }
    
        total = len(files)

        stats = {
            "total": total,
            "Imagens": 0,
            "Documentos": 0,
            "Videos": 0,
            "Compactados": 0,
            "Outros": 0
        }

        self.last_run.clear()

        self.logger.info(
            f"Iniciando organização de {total} arquivos..."
        )            

        for index, file in enumerate(files):

            try:

                # Descobre a categoria
                category = FileClassifier.classify(
                    file.suffix
                )

                # Cria o destino
                destination = (
                    Path(destination_folder)
                    / category
                )

                # Move o arquivo
                moved_to = FileMover.move_file(
                    file,
                    destination
                )

                HistoryManager.add_entry( #adiciona ao histórico
                    {
                        "file": file.name,
                        "source": str(file),
                        "destination": str(moved_to),
                        "category": category
                    }
                )

                # Guarda para desfazer depois
                self.last_run.append(
                    (
                        str(moved_to),
                        str(file)
                    )
                )

                stats["total"] += 1 
                stats[category] += 1

                self.logger.info(
                    f"{file.name} -> {category}"
                )

                # Atualiza progresso
                if progress_callback:

                    progress = (
                        (index + 1) / total
                    ) * 100

                    progress_callback(progress)

            except Exception as e:

                self.logger.error(
                    f"Erro ao mover {file.name}: {e}"
                )

        self.logger.info(
            "Organização concluída."
        )

        return stats

    def undo(self):

        for current_path, original_path in reversed(self.last_run):

            FileMover.move_file(
                Path(current_path),
                Path(original_path).parent
            )

        self.logger.info(
            "Operação desfeita"
        )

        self.last_run.clear()