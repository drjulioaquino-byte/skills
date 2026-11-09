"""Registra um caso sintético de feedback em uma pasta local."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from tempfile import NamedTemporaryFile


CAMPOS = {"skill", "revisao", "pedido", "observado", "esperado"}


def normalizar(dados):
    if not isinstance(dados, dict) or dados.keys() != CAMPOS:
        raise ValueError("Informe skill, revisao, pedido, observado e esperado.")
    if any(
        not isinstance(valor, str) or not 1 <= len(valor.strip()) <= 2000
        for valor in dados.values()
    ):
        raise ValueError("Os campos devem conter entre 1 e 2000 caracteres de texto.")

    caso = {campo: valor.strip() for campo, valor in dados.items()}
    nome = caso["skill"]
    if len(nome) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", nome):
        raise ValueError("Use o nome da pasta da skill.")
    if not re.fullmatch(r"[a-f0-9]{40}", caso["revisao"]):
        raise ValueError("Informe o SHA completo do commit da skill.")
    return caso


def registrar(destino, dados):
    caso = normalizar(dados)
    conteudo = (json.dumps(caso, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")
    identificador = hashlib.sha256(conteudo).hexdigest()
    destino.mkdir(parents=True, exist_ok=True)
    arquivo = destino / f"{identificador}.json"
    if arquivo.exists():
        if arquivo.read_bytes() != conteudo:
            raise ValueError("O registro existente diverge do conteúdo esperado.")
        return arquivo

    with NamedTemporaryFile(dir=destino, delete=False) as temporario:
        caminho_temporario = Path(temporario.name)
        try:
            temporario.write(conteudo)
            temporario.close()
            os.replace(caminho_temporario, arquivo)
        finally:
            caminho_temporario.unlink(missing_ok=True)
    return arquivo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destino", type=Path, required=True)
    parser.add_argument("entrada", type=Path)
    args = parser.parse_args()
    try:
        print(registrar(args.destino, json.loads(args.entrada.read_text(encoding="utf-8"))))
    except (OSError, ValueError) as erro:
        print(f"Registro interrompido. {erro}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
