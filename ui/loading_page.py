from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QProgressBar,
)


class LoadingPage(QWidget):

    def __init__(self):
        super().__init__()

        self._setup_ui()

    def _setup_ui(self):

        layout = QVBoxLayout(self)

        layout.setAlignment(
            Qt.AlignCenter
        )

        layout.setSpacing(25)

        self.title = QLabel(
            "Preparing your videos..."
        )

        self.title.setAlignment(
            Qt.AlignCenter
        )

        self.title.setObjectName(
            "loading_title"
        )

        layout.addWidget(
            self.title
        )

        self.progress = QProgressBar()

        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setValue(0)

        self.progress.setFixedWidth(600)

        layout.addWidget(
            self.progress
        )

        self.status = QLabel(
            "Waiting..."
        )

        self.status.setAlignment(
            Qt.AlignCenter
        )

        layout.addWidget(
            self.status
        )

    def set_paths(self, paths):

        self.paths = paths

        self.title.setText(
            "Preparing your videos..."
        )

        self.status.setText(
            f"{len(paths)} video(s) selected"
        )

        self.progress.setValue(0)