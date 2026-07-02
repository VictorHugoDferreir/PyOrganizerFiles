from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from core.file_organizer import FileOrganizer
import time

class DownloadHandler(
    FileSystemEventHandler
):

    def __init__(
        self,
        organizer,
        destination
    ):

        self.organizer = organizer
        self.destination = destination

    def wait_until_ready(self, file_path, timeout=30):

        file_path = Path(file_path)

        start = time.time()

        while time.time() - start < timeout:

            try:
                with open(file_path, "rb"):
                    return True

            except (PermissionError, FileNotFoundError):
                time.sleep(0.5)

        return False

    def on_created(self, event):

        if event.is_directory:
            return

        file_path = Path(
            event.src_path
        )
        # Ignora arquivos temporários
        if file_path.suffix.lower() in {
            ".tmp",
            ".part",
            ".crdownload"
        }:
            return

        # Espera o arquivo ficar disponível
        if not self.wait_until_ready(file_path):
            print("Arquivo não ficou disponível.")
            return
        
        try:

            self.organizer.run(
                file_path.parent,
                self.destination
            )

            print(
                f"Arquivo {file_path.name} organizado."
            )

        except Exception as e:

            print(
                f"Erro: {e}"
            )

class FolderMonitor:

    def __init__(
        self,
        source_folder,
        destination_folder,
        organizer
    ):

        self.source_folder = source_folder

        self.destination_folder = (
            destination_folder
        )

        self.organizer = organizer

        self.observer = Observer()
    
    def start(self):

        handler = DownloadHandler(
            self.organizer,
            self.destination_folder
        )

        self.observer.schedule(
            handler,
            self.source_folder,
            recursive=False
        )

        self.observer.start()

        print(
            "Monitoramento iniciado"
        )
    
    def stop(self):

        self.observer.stop()

        self.observer.join()

        print(
            "Monitoramento encerrado"
        )