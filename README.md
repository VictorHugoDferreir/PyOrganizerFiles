# 📂 PyOrganizer

Organizador inteligente de arquivos desenvolvido em Python.

O PyOrganizer automatiza a organização de arquivos em categorias, permitindo manter pastas como Downloads, Área de Trabalho ou Documentos sempre organizadas.

## 🚀 Funcionalidades

### 📁 Organização Automática

Classifica arquivos por categoria e os move para pastas específicas:

| Categoria | Extensões |
|------------|------------|
| Imagens | .jpg, .jpeg, .png, .gif |
| Documentos | .pdf, .docx, .txt, .xlsx |
| Vídeos | .mp4, .avi, .mov |
| Compactados | .zip, .rar, .7z |
| Outros | Demais extensões |

---

### 🖥️ Interface Gráfica

- Seleção de pasta de origem
- Seleção de pasta de destino
- Barra de progresso
- Status da operação
- Histórico de movimentações

---

### 💾 Configuração Persistente

O sistema salva automaticamente:

- Última pasta de origem utilizada
- Última pasta de destino utilizada

Assim o usuário não precisa configurar tudo novamente ao abrir o programa.

---

### 📜 Histórico

Todas as movimentações são registradas em:

```text
history.json
```

Permitindo consultar posteriormente:

- Nome do arquivo
- Categoria
- Destino

---

### 📝 Logs

O sistema registra eventos em:

```text
organizer.log
```

Exemplos:

```text
2025-06-16 20:30:12 - INFO - Arquivo movido: foto.jpg
2025-06-16 20:30:15 - INFO - Organização concluída
```

---

### 🔄 Desfazer Operação

Permite desfazer a última organização realizada.

---

### 👀 Pré-visualização

Exibe a categoria dos arquivos antes da movimentação.

Exemplo:

```text
foto.jpg → Imagens
contrato.pdf → Documentos
video.mp4 → Videos
```

---

### ⚡ Monitoramento Automático (Watchdog)

O sistema pode monitorar uma pasta continuamente.

Quando um novo arquivo é adicionado:

```text
Downloads
```

ele é automaticamente organizado sem intervenção do usuário.

---

## 🏗️ Arquitetura do Projeto

```text
PyOrganizer/
│
├── core/
│   ├── file_organizer.py
│   ├── file_classifier.py
│   └── folder_monitor.py
│
├── infra/
│   ├── config_loader.py
│   ├── file_mover.py
│   ├── history_manager.py
│   └── logger.py
│
├── ui/
│   └── app_window.py
│
├── config.json
├── history.json
├── organizer.log
├── main.py
└── requirements.txt
```

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Tkinter
- Pathlib
- JSON
- Logging
- Watchdog

---

## 📦 Instalação

Clone o projeto:

```bash
git clone https://github.com/seuusuario/PyOrganizer.git
```

Acesse a pasta:

```bash
cd PyOrganizer
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando

```bash
python main.py
```

---

## 📋 Dependências

```bash
pip install watchdog
```

---

## 🔮 Melhorias Futuras

- Tema escuro
- Empacotamento para .exe
- Organização baseada em IA
- Organização por data de criação
- Backup automático
- Dashboard com estatísticas

---

## 👨‍💻 Autor

Victor Hugo Dutra

Desenvolvido como projeto de portfólio para demonstrar conhecimentos em:

- Programação Orientada a Objetos
- Manipulação de Arquivos
- Interfaces Gráficas
- Persistência de Dados
- Automação com Python
