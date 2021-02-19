from __future__ import annotations

import re
import docx

_section = (lambda t : re.search('^\d [A-Z](\w*|([A-Za-z]* \w*))$', t))
_subsection = (lambda t : re.search('^\d.\d [A-Z](\w*|([A-Za-z]* \w*))$', t))
_subsubsection = (lambda t : re.search('^\d.\d.\d [A-Z](\w*|([A-Za-z]* \w*))$', t))

def unpack_docx(file):
    doc = docx.Document(file)
    full_text = []
    headers = []
    subheaders = []
    subsubheaders = []
    for para in doc.paragraphs:
        full_text.append(para.text)

    for item in full_text:
        section = _section(item)
        if section is not None:
            headers.append(section)

        subsection = _subsection(item)
        if subsection is not None:
            subheaders.append(subsection)

        subsubsection = _subsubsection(item)
        if subsubsection is not None:
            subsubheaders.append(subsubsection)

    return (full_text, headers, subheaders, subsubheaders)


if __name__ == '__main__':
    unpack_docx('/home/krummja/Workspace/Python/EpyTome/tests/test_doc.docx')
