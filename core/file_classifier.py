#Classificação de arquivos com base em suas extensões. A classe FileClassifier possui um dicionário de regras que mapeia extensões de arquivos para categorias específicas. O método classify recebe uma extensão de arquivo e retorna a categoria correspondente, ou "Outros" se a extensão não estiver presente nas regras.

class FileClassifier:

    RULES = {
        ".jpg": "Imagens",
        ".png": "Imagens",
        ".jpeg": "Imagens",
        ".pdf": "Documentos",
        ".docx": "Documentos",
        ".zip": "Compactados",
        ".mp4": "Videos",
        ".txt": "Documentos",
        ".xlsx": "Planilhas",
        ".pptx": "Apresentações",
        ".csv": "Planilhas",
    }

    @classmethod
    def classify(cls, extension):

        return cls.RULES.get(
            extension.lower(),
            "Outros"
        )