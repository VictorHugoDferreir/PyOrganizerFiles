#interface gráfica do organizador de arquivos
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

from infra.config_loader import ConfigLoader
from core.file_organizer import FileOrganizer
from infra.history_manager import HistoryManager
from core.folder_monitor import FolderMonitor


class AppWindow:

    def __init__(self, logger):

        self.logger = logger

        self.monitor = None

        self.organizer = FileOrganizer(
            logger
        )

        self.config = ConfigLoader.load_config()

        self.root = tk.Tk()

        self.root.title(
            "Organizador de Arquivos"
        )

        self.create_widgets()
        
    def update_progress(self, value):

        self.progress["value"] = value

        self.root.update_idletasks()

    def create_widgets(self):

        # Origem
        tk.Label(
            self.root,
            text="Pasta de origem"
        ).pack()

        self.source_entry = tk.Entry(
            self.root,
            width=60
        )

        self.source_entry.pack()

        self.source_entry.insert(
            0,
            self.config.get(
                "last_source",
                ""
            )
        )

        tk.Button(
            self.root,
            text="Selecionar Origem",
            command=self.select_source
        ).pack(pady=5)

        # Destino
        tk.Label(
            self.root,
            text="Pasta de destino"
        ).pack()

        self.destination_entry = tk.Entry(
            self.root,
            width=60
        )

        self.destination_entry.pack()

        self.destination_entry.insert(
            0,
            self.config.get(
                "last_destination",
                ""
            )
        )

        tk.Button(
            self.root,
            text="Selecionar Destino",
            command=self.select_destination
        ).pack(pady=5)

        # Botão Organizar
        self.btn_run = tk.Button(
            self.root,
            text="Organizar",
            command=self.organize
        )

        #Botão Desfazer
        self.undo_button = tk.Button(
            self.root,
            text="Desfazer Última Organização",
            command=self.undo
        )

        self.undo_button.pack(pady=5)

        self.history_button = tk.Button( #botão para mostrar o histórico de organização, que exibe uma janela com as informações dos arquivos organizados, incluindo nome do arquivo, pasta de origem, pasta de destino e categoria. O histórico é carregado usando o HistoryManager e exibido em um formato legível para o usuário.
            self.root,
            text="Ver Histórico",
            command=self.show_history
        )

        self.history_button.pack(pady=5)

        #Botão Monitorar
        self.monitor_button = tk.Button(
            self.root,
            text="Iniciar Monitoramento",
            command=self.start_monitor
        )

        self.monitor_button.pack(
            pady=5
        )

        # Barra de progresso
        self.progress = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=400,
            mode="determinate"
        )

        self.progress.pack(pady=10)

        self.btn_run.pack(pady=20)
        self.btn_run.pack()

        self.status_label = tk.Label(
        self.root,
        text="Pronto"
        )

        self.status_label.pack()

    def select_source(self): #seleciona a pasta de origem usando um diálogo de seleção de diretório. Se o usuário selecionar uma pasta, o caminho da pasta é inserido no campo de entrada correspondente na interface gráfica.

        folder = filedialog.askdirectory()

        if folder:
            self.source_entry.delete(0, tk.END)
            self.source_entry.insert(0, folder)

    def select_destination(self): #seleciona a pasta de destino usando um diálogo de seleção de diretório. Se o usuário selecionar uma pasta, o caminho da pasta é inserido no campo de entrada correspondente na interface gráfica.

        folder = filedialog.askdirectory()

        if folder:
            self.destination_entry.delete(0, tk.END)
            self.destination_entry.insert(0, folder)
    
    def organize(self):

        source = self.source_entry.get()
        destination = self.destination_entry.get()

        try:
            if not source:      #valida se os campos estão preenchidos
                messagebox.showwarning(
                    "Aviso",
                    "Selecione uma pasta de origem."
                )
                return

            if not destination:
                messagebox.showwarning(
                    "Aviso",
                    "Selecione uma pasta de destino."
                )
                return

            ConfigLoader.save_config( #salva as últimas pastas usadas para facilitar o uso futuro
                {
                    "last_source": source,
                    "last_destination": destination
                }
            )

            self.status_label.config(
                text="Organizando..."
            )

            stats = self.organizer.run(
                source,
                destination,
                self.update_progress
            )

            self.progress["value"] = 0

            self.status_label.config(
                text=f"{stats['total']} arquivos organizados"
            )
            
            self.stats_label.config(
                text=
                f"📷 Imagens: {stats['Imagens']}\n"
                f"📄 Documentos: {stats['Documentos']}\n"
                f"🎬 Videos: {stats['Videos']}\n"
                f"📦 Compactados: {stats['Compactados']}\n"
                f"📁 Outros: {stats['Outros']}"
            )
            
            messagebox.showinfo(
                "Sucesso",
                "Arquivos organizados com sucesso!"
            )

        except Exception as e:

            messagebox.showerror(
                "Erro",
                str(e)
            )

            self.status_label.config(
                text="Erro"
            )
    def show_history(self):

        history = HistoryManager.load_history()

        history_window = tk.Toplevel(
            self.root
        )

        history_window.title(
            "Histórico de Organizações"
        )

        history_window.geometry(
            "800x400"
        )

        scrollbar = tk.Scrollbar(
        history_window
        )

        scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        listbox = tk.Listbox(
            history_window,
            width=120,
            height=20,
            yscrollcommand=scrollbar.set
        )

        listbox.pack(
            fill=tk.BOTH,
            expand=True
        )

        scrollbar.config(
            command=listbox.yview
        )
        if not history:

            listbox.insert(
                tk.END,
                "Nenhum histórico encontrado."
            )

            return

        for entry in history:

            listbox.insert(
                tk.END,
                f"{entry['file']}  →  {entry['category']}"
            )

    def undo(self):

        try: #permite desfazer a última organização, movendo os arquivos de volta para suas localizações originais usando as informações armazenadas durante a execução anterior. Se ocorrer algum erro durante o processo de desfazer, uma mensagem de erro será exibida.

            self.organizer.undo()

            messagebox.showinfo(
                "Sucesso",
                "Operação desfeita."
            )

        except Exception as e:

            messagebox.showerror(
                "Erro",
                str(e)
            )

    def start(self):
        self.root.mainloop()

    def start_monitor(self):

        source = self.source_entry.get()

        destination = (
            self.destination_entry.get()
        )

        self.monitor = FolderMonitor(
            source,
            destination,
            self.organizer
        )

        self.monitor.start()

        self.status_label.config(
            text="Monitorando..."
        )