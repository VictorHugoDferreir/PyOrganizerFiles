from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from core.file_organizer import FileOrganizer

from pathlib import Path
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

    def on_created(self, event):

        if event.is_directory:
            return

        file_path = Path(
            event.src_path
        )

        print(
            f"Novo arquivo: {file_path.name}"
        )
    try:

        self.organizer.run(
            file_path.parent,
            self.destination
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