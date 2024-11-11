from pathlib import Path
import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    path_file = Path(path_file)
    if path_file.suffix != '.txt':
        print('Formato inválido', file=sys.stderr)
        return
    try:
        with open(path_file, 'r', encoding='utf8') as file:
            return file.read().split('\n')
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
