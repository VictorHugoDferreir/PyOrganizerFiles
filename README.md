# 📂 PyOrganizerFiles

Um organizador inteligente de arquivos desenvolvido em **Python**, com interface gráfica, monitoramento em tempo real e organização automática por categorias.

O objetivo do projeto é automatizar a organização de pastas como **Downloads**, **Documentos** ou qualquer outra pasta escolhida pelo usuário, tornando a gestão de arquivos mais prática e eficiente.

---

## ✨ Funcionalidades

- 📁 Organização automática por categoria
- 🖥️ Interface gráfica desenvolvida com Tkinter
- 📊 Barra de progresso durante a organização
- 📜 Histórico das movimentações realizadas
- ↩️ Desfazer última organização
- 💾 Salvamento automático da última pasta utilizada
- 📝 Sistema de logs para auditoria das operações
- 👀 Monitoramento automático de pastas com Watchdog
- 📄 Estatísticas da organização realizada
- 🔄 Tratamento de conflitos de nomes de arquivos

---

## 📂 Categorias suportadas

O sistema identifica automaticamente diversas extensões de arquivos.

| Categoria | Exemplos |
|-----------|-----------|
| 🖼️ Imagens | .jpg, .jpeg, .png, .gif |
| 📄 Documentos | .pdf, .docx, .txt |
| 📊 Planilhas | .xls, .xlsx, .csv |
| 📽️ Vídeos | .mp4, .avi, .mov |
| 📦 Compactados | .zip, .rar, .7z |
| 📽️ Apresentações | .ppt, .pptx |
| 📁 Outros | Demais extensões |

---

## ⚙️ Como funciona

### Organização Manual

O usuário seleciona:

- Pasta de origem
- Pasta de destino

Ao clicar em **Organizar**, todos os arquivos são classificados e movidos automaticamente para suas respectivas categorias.

---

### Monitoramento Automático

Ao ativar o monitoramento, o programa permanece observando a pasta de origem.

Sempre que um novo arquivo é criado:

```
Downloads
    ↓
novo_arquivo.pdf
    ↓
Watchdog detecta
    ↓
PyOrganizer organiza automaticamente
```

Não é necessário executar a organização manualmente.

---

## 🏗️ Arquitetura

```
PyOrganizerFiles/
│
├── core/
│   ├── file_classifier.py
│   ├── file_organizer.py
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

## 🛠️ Tecnologias utilizadas

- Python 3
- Tkinter
- Watchdog
- Pathlib
- JSON
- Logging
- shutil

---

## 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/PyOrganizerFiles.git
```

Entre na pasta:

```bash
cd PyOrganizerFiles
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

## 📦 Dependências

```text
watchdog
```

ou

```bash
pip install watchdog
```

---

## 📸 Interface

> Adicione aqui um print da aplicação.

Exemplo:

```
assets/
    screenshot.png
```

```markdown
![Interface](assets/screenshot.png)
```

---

## 📈 Melhorias Futuras

- [ ] Tema escuro
- [ ] Organização personalizada por regras
- [ ] Exportação do histórico para CSV
- [ ] Notificações do Windows
- [ ] Organização por data
- [ ] Empacotamento para executável (.exe)

---

## 👨‍💻 Autor

**Victor Hugo Dutra**

Projeto desenvolvido para praticar:

- Programação Orientada a Objetos
- Manipulação de Arquivos
- Interface Gráfica com Tkinter
- Automação com Python
- Arquitetura em Camadas