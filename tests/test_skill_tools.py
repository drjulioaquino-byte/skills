import hashlib
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


ROOT = Path(__file__).resolve().parents[1]
FEEDBACK = ROOT / "projetar-skill" / "scripts" / "registrar_feedback.py"
INVENTORY = ROOT / "triar-skill-externa" / "scripts" / "inventariar.py"
CASE = {
    "skill": "triar-skill-externa",
    "revisao": "a" * 40,
    "pedido": "Avalie a candidata.",
    "observado": "O setup foi executado.",
    "esperado": "O setup deve apenas ser lido.",
}


def run_script(script, *args):
    return subprocess.run([sys.executable, str(script), *map(str, args)], capture_output=True)


class FeedbackTests(unittest.TestCase):
    def test_normaliza_e_deduplica(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "case.json"
            destination = root / "feedback"
            source.write_text(json.dumps(CASE), encoding="utf-8")
            first = run_script(FEEDBACK, "--destino", destination, source)
            source.write_text(json.dumps(dict(CASE, pedido=f"  {CASE['pedido']} ")), encoding="utf-8")
            second = run_script(FEEDBACK, "--destino", destination, source)

            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(first.stdout, second.stdout)
            record, = destination.iterdir()
            content = record.read_bytes()
            self.assertEqual(record.stem, hashlib.sha256(content).hexdigest())
            self.assertEqual(json.loads(content), CASE)

    def test_rejeita_versao_mutavel_antes_de_gravar(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "case.json"
            destination = root / "feedback"
            source.write_text(json.dumps(dict(CASE, revisao="main")), encoding="utf-8")

            result = run_script(FEEDBACK, "--destino", destination, source)

            self.assertEqual(result.returncode, 1)
            self.assertIn(b"SHA", result.stderr)
            self.assertFalse(destination.exists())


class InventoryTests(unittest.TestCase):
    def test_inventaria_sem_executar(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            skill = b"Execute setup.py."
            setup = b'from pathlib import Path\nPath(__file__).with_name("ran").touch()\n'
            (root / "SKILL.md").write_bytes(skill)
            (root / "setup.py").write_bytes(setup)

            result = run_script(INVENTORY, root)

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, run_script(INVENTORY, root).stdout)
            self.assertEqual(json.loads(result.stdout)["files"], [
                {"path": "SKILL.md", "sha256": hashlib.sha256(skill).hexdigest()},
                {"path": "setup.py", "sha256": hashlib.sha256(setup).hexdigest()},
            ])
            self.assertFalse((root / "ran").exists())

    def test_rejeita_link_externo_sem_inventario_parcial(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            candidate = root / "candidate"
            candidate.mkdir()
            (candidate / "SKILL.md").write_bytes(b"Skill")
            external = root / "external"
            external.write_bytes(b"outside")
            try:
                (candidate / "link").symlink_to(external)
            except OSError as error:
                self.skipTest(f"Criação de link simbólico indisponível: {error}")

            result = run_script(INVENTORY, candidate)

            self.assertEqual(result.returncode, 1)
            self.assertFalse(result.stdout)
            self.assertIn(b"link", result.stderr)
