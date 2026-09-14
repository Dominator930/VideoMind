import os
from PySide6.QtCore import Signal, Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QFrame,
    QProgressBar,
)

from .settings_dialog import SettingsDialog


class WelcomePage(QWidget):

    files_selected = Signal(list)
    theme_toggled = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_dark_theme = False

        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(25, 20, 25, 20)
        main_layout.setSpacing(20)

        # -------------------------
        # Header (Top Bar)
        # -------------------------
        self.header = QLabel("Welcome To VideoMind")
        self.header.setAlignment(Qt.AlignCenter)
        self.header.setObjectName("header")
        main_layout.addWidget(self.header)

        main_layout.addStretch()

        # -------------------------
        # Center Workspace (Selection Card + Loading Screen)
        # -------------------------
        center_container = QWidget()
        center_layout = QVBoxLayout(center_container)
        center_layout.setAlignment(Qt.AlignCenter)
        center_layout.setSpacing(25)

        # 1. Select File / Folder Area
        self.selection_card = QFrame()
        self.selection_card.setObjectName("selection_card")
        self.selection_card.setFixedWidth(650)
        self.selection_card.setMinimumHeight(160)

        card_layout = QVBoxLayout(self.selection_card)
        card_layout.setAlignment(Qt.AlignCenter)
        card_layout.setContentsMargins(30, 25, 30, 25)

        self.select_button = QPushButton("Select File / Folder")
        self.select_button.setObjectName("select_button")
        self.select_button.setMinimumHeight(65)
        self.select_button.setFixedWidth(450)

        card_layout.addWidget(self.select_button)
        center_layout.addWidget(self.selection_card)

        # 2. Loading Screen Area (Progress indicator box)
        self.loading_card = QFrame()
        self.loading_card.setObjectName("loading_card")
        self.loading_card.setFixedWidth(650)
        self.loading_card.setMinimumHeight(140)

        loading_layout = QVBoxLayout(self.loading_card)
        loading_layout.setAlignment(Qt.AlignCenter)
        loading_layout.setContentsMargins(25, 20, 25, 20)
        loading_layout.setSpacing(12)

        self.loading_title = QLabel("Loading Screen")
        self.loading_title.setObjectName("loading_title")
        self.loading_title.setAlignment(Qt.AlignCenter)

        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setValue(0)
        self.progress.setFixedWidth(550)

        self.loading_status = QLabel("Select a video file or parquet database to begin processing")
        self.loading_status.setObjectName("loading_status")
        self.loading_status.setAlignment(Qt.AlignCenter)

        loading_layout.addWidget(self.loading_title)
        loading_layout.addWidget(self.progress)
        loading_layout.addWidget(self.loading_status)

        center_layout.addWidget(self.loading_card)
        main_layout.addWidget(center_container)

        main_layout.addStretch()

        # -------------------------
        # Bottom Bar (Theme Toggler & Settings)
        # -------------------------
        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(10, 10, 10, 5)

        # Theme Toggler Circular Button
        self.theme_button = QPushButton()
        self.theme_button.setObjectName("theme_button")
        self.theme_button.setFixedSize(50, 50)
        self.theme_button.setToolTip("Toggle Light / Dark Theme")
        self.update_theme_icon(self.is_dark_theme)

        bottom_layout.addWidget(self.theme_button, alignment=Qt.AlignLeft)
        bottom_layout.addStretch()

        # Settings Circular Button
        self.settings_button = QPushButton()
        self.settings_button.setObjectName("settings_button")
        self.settings_button.setFixedSize(50, 50)
        self.settings_button.setToolTip("Open VideoMind Settings")

        assets_dir = os.path.join(os.path.dirname(__file__), "assets")
        gear_icon_path = os.path.join(assets_dir, "gear.svg")
        if os.path.exists(gear_icon_path):
            self.settings_button.setIcon(QIcon(gear_icon_path))
            self.settings_button.setIconSize(QSize(24, 24))
        else:
            self.settings_button.setText("⚙")

        bottom_layout.addWidget(self.settings_button, alignment=Qt.AlignRight)
        main_layout.addLayout(bottom_layout)

    def update_theme_icon(self, is_dark):
        self.is_dark_theme = is_dark
        assets_dir = os.path.join(os.path.dirname(__file__), "assets")
        icon_file = "sun.svg" if is_dark else "moon.svg"
        icon_path = os.path.join(assets_dir, icon_file)

        if os.path.exists(icon_path):
            self.theme_button.setIcon(QIcon(icon_path))
            self.theme_button.setIconSize(QSize(24, 24))
            self.theme_button.setText("")
        else:
            self.theme_button.setText("☀" if is_dark else "🌙")

    def _connect_signals(self):
        self.select_button.clicked.connect(self.select_source)
        self.theme_button.clicked.connect(lambda: self.theme_toggled.emit())
        self.settings_button.clicked.connect(self.open_settings)

    def select_source(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilters([
            "Supported Files (*.mp4 *.mkv *.avi *.mov *.webm *.parquet)",
            "Video Files (*.mp4 *.mkv *.avi *.mov *.webm)",
            "Parquet Files (*.parquet)",
            "All Files (*)"
        ])

        if file_dialog.exec():
            paths = file_dialog.selectedFiles()
            if paths:
                self.files_selected.emit(paths)

    def open_settings(self):
        dialog = SettingsDialog(self)
        dialog.exec()

    def update_progress(self, value, message):
        self.progress.setValue(value)
        self.loading_status.setText(message)
        if value < 100:
            self.loading_title.setText(f"Preparing your videos... ({value}%)")
        else:
            self.loading_title.setText("Processing Complete!")