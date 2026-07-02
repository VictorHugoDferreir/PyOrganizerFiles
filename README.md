<<<<<<< HEAD
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
=======
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
>>>>>>> c9d8c3a5941c0df16d3ad322527a053142e19fea
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

<<<<<<< HEAD
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
=======
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
>>>>>>> c9d8c3a5941c0df16d3ad322527a053142e19fea
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

<<<<<<< HEAD
## 📦 Dependências

```text
watchdog
```

ou
=======
## 📋 Dependências
>>>>>>> c9d8c3a5941c0df16d3ad322527a053142e19fea

```bash
pip install watchdog
```

---

<<<<<<< HEAD
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
=======
## 🔮 Melhorias Futuras

- Tema escuro
- Empacotamento para .exe
- Organização baseada em IA
- Organização por data de criação
- Backup automático
- Dashboard com estatísticas
>>>>>>> c9d8c3a5941c0df16d3ad322527a053142e19fea

---

## 👨‍💻 Autor

<<<<<<< HEAD
**Victor Hugo Dutra**

Projeto desenvolvido para praticar:

- Programação Orientada a Objetos
- Manipulação de Arquivos
- Interface Gráfica com Tkinter
- Automação com Python
- Arquitetura em Camadas
=======
Victor Hugo Dutra

Desenvolvido como projeto de portfólio para demonstrar conhecimentos em:

- Programação Orientada a Objetos
- Manipulação de Arquivos
- Interfaces Gráficas
- Persistência de Dados
- Automação com Python
>>>>>>> c9d8c3a5941c0df16d3ad322527a053142e19fea
