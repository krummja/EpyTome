from __future__ import annotations

from epytome.gui import Application
from epytome.document import unpack_docx

if __name__ == '__main__':

    result = unpack_docx('/home/krummja/Workspace/Python/EpyTome/epytome/assets/test_doc.docx')
    print(result)

    app = Application()
    app.start()
