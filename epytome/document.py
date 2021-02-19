from __future__ import annotations

from collections import defaultdict
import pylatex
import docx


def unpack_docx(file):
    doc = docx.Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)



class Section:

    def __init__(self, document: Document) -> None:
        self.document = document


class Document:

    def __init__(self, file: str) -> None:
        self.file = file
        self.sections = defaultdict()
