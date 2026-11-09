"""Inventaria uma pasta de skill sem executar o seu conteúdo."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import sys


def tipo_seguro(caminho):
    info = caminho.lstat()
    atributos = getattr(info, "st_file_attributes", 0)
    if stat.S_ISLNK(info.st_mode) or atributos & stat.FILE_ATTRIBUTE_REPARSE_POINT:
        raise ValueError(f"Link ou ponto de nova análise: {caminho}")
    return info.st_mode


def inventariar(raiz):
    caminho = raiz.absolute()
    for parte in (*reversed(caminho.parents), caminho):
        if not stat.S_ISDIR(tipo_seguro(parte)):
            raise ValueError(f"Diretório esperado: {parte}")

    if not stat.S_ISREG(tipo_seguro(caminho / "SKILL.md")):
        raise ValueError("SKILL.md deve ser um arquivo regular.")

    def falhar(erro):
        raise erro

    arquivos = []
    for pasta, subpastas, nomes in os.walk(caminho, onerror=falhar):
        diretorio = Path(pasta)
        for nome in subpastas:
            subpasta = diretorio / nome
            if not stat.S_ISDIR(tipo_seguro(subpasta)):
                raise ValueError(f"Diretório esperado: {subpasta}")
        for nome in nomes:
            arquivo = diretorio / nome
            if not stat.S_ISREG(tipo_seguro(arquivo)):
                raise ValueError(f"Arquivo regular esperado: {arquivo}")
            with arquivo.open("rb") as entrada:
                digest = hashlib.file_digest(entrada, "sha256").hexdigest()
            arquivos.append({"path": arquivo.relative_to(caminho).as_posix(), "sha256": digest})

    return sorted(arquivos, key=lambda item: item["path"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pasta", type=Path, help="Pasta isolada que contém SKILL.md")
    args = parser.parse_args()
    try:
        arquivos = inventariar(args.pasta)
    except (OSError, ValueError) as erro:
        print(f"Inventário interrompido. {erro}", file=sys.stderr)
        return 1

    print(json.dumps({"files": arquivos}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
