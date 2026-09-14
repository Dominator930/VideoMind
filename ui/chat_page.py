import os
from PySide6.QtCore import Signal, Qt, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QListWidget,
    QLineEdit,
    QFrame,
    QScrollArea,
    QTextBrowser,
)

from .settings_dialog import SettingsDialog


class ChatPage(QWidget):
    query_submitted = Signal(str)
    theme_toggled = Signal()
    back_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_dark_theme = False

        self._setup_ui()
        self._connect_signals()

    def _setup_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # -------------------------
        # Header (Top Bar)
        # -------------------------
        header_widget = QWidget()
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(20, 12, 20, 12)

        self.back_button = QPushButton("← Switch Video")
        self.back_button.setObjectName("header_back_btn")
        header_layout.addWidget(self.back_button, alignment=Qt.AlignLeft)

        header_title = QLabel("Welcome To VideoMind")
        header_title.setObjectName("header")
        header_title.setAlignment(Qt.AlignCenter)
        header_layout.addWidget(header_title, 1)

        # Invisible placeholder for title alignment balance
        dummy_btn = QWidget()
        dummy_btn.setFixedWidth(100)
        header_layout.addWidget(dummy_btn)

        main_layout.addWidget(header_widget)

        # -------------------------
        # Body (Sources Sidebar + Chat Workspace)
        # -------------------------
        body_widget = QWidget()
        body_layout = QHBoxLayout(body_widget)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        # Left Sidebar (Sources Panel)
        self.sidebar = QWidget()
        self.sidebar.setObjectName("sidebar_container")
        self.sidebar.setFixedWidth(250)

        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        sidebar_layout.setSpacing(8)

        sources_title = QLabel("Sources")
        sources_title.setObjectName("sources_title")
        sidebar_layout.addWidget(sources_title)

        self.sources = QListWidget()
        self.sources.setObjectName("sources")
        sidebar_layout.addWidget(self.sources)

        body_layout.addWidget(self.sidebar)

        # Center Workspace (Chat Area + Bottom Input)
        chat_workspace = QWidget()
        workspace_layout = QVBoxLayout(chat_workspace)
        workspace_layout.setContentsMargins(0, 0, 0, 0)
        workspace_layout.setSpacing(0)

        # Chat Message Scroll Area (Gemini / Claude style)
        self.scroll_area = QScrollArea()
        self.scroll_area.setObjectName("chat_scroll_area")
        self.scroll_area.setWidgetResizable(True)

        self.chat_container = QWidget()
        self.chat_container.setObjectName("chat_scroll_widget")
        self.chat_layout = QVBoxLayout(self.chat_container)
        self.chat_layout.setContentsMargins(30, 20, 30, 20)
        self.chat_layout.setSpacing(18)
        self.chat_layout.addStretch()

        self.scroll_area.setWidget(self.chat_container)
        workspace_layout.addWidget(self.scroll_area, 1)

        # Bottom Input Bar
        input_bar_frame = QFrame()
        input_bar_frame.setObjectName("input_bar_frame")
        input_bar_layout = QHBoxLayout(input_bar_frame)
        input_bar_layout.setContentsMargins(25, 12, 25, 12)
        input_bar_layout.setSpacing(12)

        self.question_input = QLineEdit()
        self.question_input.setObjectName("question_input")
        self.question_input.setPlaceholderText("Ask VideoMind about your videos...")

        self.send_button = QPushButton("Send")
        self.send_button.setObjectName("send_button")

        input_bar_layout.addWidget(self.question_input, 1)
        input_bar_layout.addWidget(self.send_button)

        workspace_layout.addWidget(input_bar_frame)
        body_layout.addWidget(chat_workspace, 1)
        main_layout.addWidget(body_widget, 1)

        # -------------------------
        # Bottom Bar (Theme Toggler & Settings)
        # -------------------------
        bottom_bar = QWidget()
        bottom_layout = QHBoxLayout(bottom_bar)
        bottom_layout.setContentsMargins(15, 8, 15, 12)

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
        main_layout.addWidget(bottom_bar)

    def _connect_signals(self):
        self.back_button.clicked.connect(lambda: self.back_requested.emit())
        self.send_button.clicked.connect(self._on_send)
        self.question_input.returnPressed.connect(self._on_send)
        self.theme_button.clicked.connect(lambda: self.theme_toggled.emit())
        self.settings_button.clicked.connect(self.open_settings)

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

    def open_settings(self):
        dialog = SettingsDialog(self)
        dialog.exec()

    def set_input_enabled(self, enabled: bool):
        self.is_busy = not enabled
        self.question_input.setEnabled(enabled)
        self.send_button.setEnabled(enabled)
        if enabled:
            self.question_input.setPlaceholderText("Ask VideoMind about your videos...")
            self.question_input.setFocus()
        else:
            self.question_input.setPlaceholderText("VideoMind is generating a response... Please wait.")

    def set_sources(self, paths):
        self.sources.clear()
        for p in paths:
            self.sources.addItem(os.path.basename(p))
        self.set_input_enabled(True)

    def _on_send(self):
        if getattr(self, "is_busy", False):
            return
        text = self.question_input.text().strip()
        if text:
            self.set_input_enabled(False)
            self.add_user_message(text)
            self.question_input.clear()
            self.show_thinking(True)
            self.query_submitted.emit(text)

    def add_user_message(self, message):
        # Container to align user bubble to right
        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.addStretch()

        bubble = QFrame()
        bubble.setObjectName("user_bubble")
        bubble_layout = QVBoxLayout(bubble)
        bubble_layout.setContentsMargins(14, 10, 14, 10)

        label = QLabel(message)
        label.setObjectName("user_bubble_text")
        label.setWordWrap(True)
        label.setMaximumWidth(600)

        bubble_layout.addWidget(label)
        row.addWidget(bubble)

        # Insert before stretch
        count = self.chat_layout.count()
        self.chat_layout.insertLayout(count - 1, row)
        self._scroll_to_bottom()

    def add_ai_message(self, html_content):
        self.show_thinking(False)
        self.set_input_enabled(True)

        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)

        card = QFrame()
        card.setObjectName("ai_card")
        card.setMaximumWidth(750)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(16, 14, 16, 14)
        card_layout.setSpacing(8)

        avatar = QLabel("✦ VideoMind AI")
        avatar.setObjectName("ai_avatar_label")
        card_layout.addWidget(avatar)

        browser = QTextBrowser()
        browser.setObjectName("ai_card_text")
        browser.setOpenExternalLinks(True)
        browser.setHtml(html_content.replace("\n", "<br>"))

        # Adjust height based on content
        browser.document().adjustSize()
        h = max(60, int(browser.document().size().height()) + 20)
        browser.setMinimumHeight(min(h, 450))

        card_layout.addWidget(browser)
        row.addWidget(card)
        row.addStretch()

        count = self.chat_layout.count()
        self.chat_layout.insertLayout(count - 1, row)
        self._scroll_to_bottom()

    def show_thinking(self, show=True):
        if show:
            if not hasattr(self, "thinking_card") or self.thinking_card is None:
                self.thinking_row = QHBoxLayout()
                self.thinking_card = QFrame()
                self.thinking_card.setObjectName("ai_card")

                layout = QHBoxLayout(self.thinking_card)
                lbl = QLabel("✦ VideoMind is thinking...")
                lbl.setObjectName("ai_avatar_label")
                layout.addWidget(lbl)

                self.thinking_row.addWidget(self.thinking_card)
                self.thinking_row.addStretch()

                count = self.chat_layout.count()
                self.chat_layout.insertLayout(count - 1, self.thinking_row)
            self._scroll_to_bottom()
        else:
            if hasattr(self, "thinking_card") and self.thinking_card:
                self.thinking_card.deleteLater()
                self.thinking_card = None

    def _scroll_to_bottom(self):
        self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().maximum()
        )
