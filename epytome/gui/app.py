from __future__ import annotations

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import os
import sys
import uuid


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.path = None

        CONTAINER = QWidget()
        LAYOUT = QVBoxLayout()
        CONTAINER.setLayout(LAYOUT)
        STATUS = QStatusBar()
        self.setStatusBar(STATUS)

        #! - Toolbar
        TOOLBAR = QToolBar("Toolbar")
        TOOLBAR.setIconSize(QSize(14, 14))
        self.addToolBar(TOOLBAR)

        #! -- Open File
        open_file_action = QAction("Add", self)
        open_file_action.setStatusTip("Add")
        open_file_action.triggered.connect(self.file_open)
        TOOLBAR.addAction(open_file_action)

        self.update_title()
        self.show()

    def file_open(self):
        file_types = ""
        file_types += "Text documents (*.txt);;"
        file_types += "Markdown documents (*.md);;"
        file_types += "LaTeX documents (*.tex);;"
        file_types += "BibTeX documents (*.bib);;"
        file_types += "All files (*.*)"

        path, _ = QFileDialog.getOpenFileName(self, "Add", "", file_types)

        try:
            with open(path, 'rU') as f:
                text = f.read()
        except Exception as e:
            self.dialog_critical(str(e))
        else:
            self.path = path
            self.update_title()

    def dialog_critical(self, error: str):
        dlg = QMessageBox(self)
        dlg.setText(error)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def file_save(self):
        pass

    def update_title(self):
        self.setWindowTitle(f"EpyTome - {os.path.basename(self.path) if self.path else ''}")


class Application:
    root = QApplication(sys.argv)
    root.setApplicationName("EpyTome")
    window = MainWindow()

    def start(self) -> None:
        self.root.exec_()
