# Organizador de Downloads

Script Python que organiza a pasta Downloads movendo arquivos para subpastas por tipo (Imagens, Documentos, Vídeos, etc.).

## O que faz

- Lê todos os arquivos da pasta escolhida
- Identifica a extensão de cada arquivo
- Move para uma subpasta baseada na categoria:

| Categoria | Extensões |
|---|---|
| Imagens | .jpg, .jpeg, .png, .gif, .bmp |
| Documentos | .pdf, .docx, .txt, .xlsx |
| Vídeos | .mp4, .avi, .mkv, .mov |
| Músicas | .mp3, .wav, .flac |
| Compactados | .zip, .rar, .7z |

## Como usar

1. Instale o Python (versão 3.8 ou superior)
2. Baixe o arquivo `organizer.py`
3. Abra o arquivo e mude o caminho no final:

```python
organizar("C:/Users/SeuUsuario/Downloads")