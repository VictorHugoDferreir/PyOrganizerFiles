#interface gráfica do organizador de arquivos
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

from PyOrganizer.infra.config_loader import ConfigLoader
from core.file_organizer import FileOrganizer


class AppWindow:

    def __init__(self, logger):

        self.logger = logger

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

            self.organizer.run(
                source,
                destination,
                self.update_progress
            )

            self.status_label.config(
                text="Concluído!"
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