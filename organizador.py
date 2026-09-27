import shutil
from pathlib import Path

CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Vídeos": [".mp4", ".avi", ".mkv", ".mov"],
    "Músicas": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z"],
}


def organizar(pasta):
    pasta = Path(pasta)

    for arquivo in pasta.iterdir():
        if arquivo.is_file():
            extensao = arquivo.suffix.lower()

            for categoria, extensoes in CATEGORIAS.items():
                if extensao in extensoes:
                    destino = pasta / categoria
                    destino.mkdir(exist_ok=True)

                    try:
                        shutil.move(str(arquivo), str(destino / arquivo.name))
                        print(f"Movido: {arquivo.name} → {categoria}/")
                    except Exception as e:
                        print(f"Erro ao mover {arquivo.name}: {e}")

                    break


if __name__ == "__main__":
    organizar("C:/msys64/home/Projetos/Organizador_de_Downloads/teste_downloads")