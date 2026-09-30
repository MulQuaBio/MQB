"""Focused checks for the published-source integrity checker."""

import tempfile
import unittest
from pathlib import Path

import nbformat

from check_content import check_book


class CheckContentTests(unittest.TestCase):
    def test_toc_and_notebook_references(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            book = root / "content"
            (book / "notebooks").mkdir(parents=True)
            (book / "data").mkdir()
            (book / "_toc.yml").write_text("root: intro\nchapters:\n- file: notebooks/example\n")
            (book / "intro.md").write_text("[Example](notebooks/example.ipynb)\n")
            (book / "data" / "pound_hill_data.csv").write_text("count\n1\n")
            notebook = nbformat.v4.new_notebook(
                cells=[nbformat.v4.new_markdown_cell("[Intro](../intro.md)"),
                       nbformat.v4.new_code_cell("read.csv('../data/PoundHillData.csv')")],
                metadata={"kernelspec": {"name": "ir", "display_name": "R"}},
            )
            nbformat.write(notebook, book / "notebooks" / "example.ipynb")
            ledger = root / "mapping.tsv"
            ledger.write_text("content/data/PoundHillData.csv\tcontent/data/pound_hill_data.csv\n")

            problems = check_book(book, ledger)

            self.assertTrue(any("missing exact-case path ../data/PoundHillData.csv" in item for item in problems))
            self.assertTrue(any("old data filename PoundHillData.csv" in item for item in problems))
            self.assertFalse(any("missing link" in item for item in problems))
            notebook.cells[1].source = "read.csv('../data/pound_hill_data.csv')"
            nbformat.write(notebook, book / "notebooks" / "example.ipynb")
            self.assertEqual(check_book(book, ledger), [])

    def test_missing_toc_link_and_kernel(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            book = root / "content"
            book.mkdir()
            (book / "_toc.yml").write_text("root: intro\nchapters:\n- file: absent\n")
            (book / "intro.md").write_text("[Missing](absent.md)\n")
            ledger = root / "mapping.tsv"
            ledger.write_text("")
            issues = check_book(book, ledger)
            self.assertTrue(any("missing page absent" in issue for issue in issues))
            self.assertTrue(any("missing link absent.md" in issue for issue in issues))

            (book / "_toc.yml").write_text("root: intro\nchapters:\n- file: example\n")
            (book / "intro.md").write_text("[Example](example.ipynb)\n")
            notebook = nbformat.v4.new_notebook(cells=[nbformat.v4.new_markdown_cell(
                "Illustrative path: ../data/example.csv")])
            nbformat.write(notebook, book / "example.ipynb")
            self.assertEqual(check_book(book, ledger), [])
            notebook.cells.append(nbformat.v4.new_code_cell("1 + 1"))
            nbformat.write(notebook, book / "example.ipynb")
            self.assertEqual(check_book(book, ledger), ["example.ipynb: missing kernel name"])
            (book / "example.ipynb").write_text("not a notebook")
            self.assertTrue(any("invalid notebook" in issue for issue in check_book(book, ledger)))


if __name__ == "__main__":
    unittest.main()