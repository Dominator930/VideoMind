import os
import atexit
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QStackedWidget,
    QMessageBox,
)

from .welcome_page import WelcomePage
from .chat_page import ChatPage
from .theme import LIGHT_THEME, DARK_THEME
from .worker import VideoProcessorWorker, QueryWorker
from backend.src.essential_functions import delete_files_and_create_parquet


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("VideoMind")
        self.setMinimumSize(1050, 720)
        self.is_dark_theme = False
        self.current_file_name = None
        self._cleaned_up = False

        self._setup_ui()
        self._connect_signals()
        self.apply_theme(self.is_dark_theme)

        # Register exit cleanup
        atexit.register(self.cleanup)

    def _setup_ui(self):
        self.central_widget = QWidget()
        self.central_widget.setObjectName("central_widget")

        layout = QVBoxLayout(self.central_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self.pages = QStackedWidget()

        # Screen 1: Welcome / Selection / Loading Page
        self.welcome_page = WelcomePage()
        
        # Screen 2: Gemini/Claude Style Chat Page
        self.chat_page = ChatPage()

        self.pages.addWidget(self.welcome_page)
        self.pages.addWidget(self.chat_page)

        layout.addWidget(self.pages)
        self.setCentralWidget(self.central_widget)

    def _connect_signals(self):
        # Navigation & Actions
        self.welcome_page.files_selected.connect(self.process_selected_files)
        self.chat_page.back_requested.connect(self.show_welcome_page)
        self.chat_page.query_submitted.connect(self.process_user_query)

        # Theme toggling from both screens
        self.welcome_page.theme_toggled.connect(self.toggle_theme)
        self.chat_page.theme_toggled.connect(self.toggle_theme)

    def cleanup(self):
        if not self._cleaned_up:
            self._cleaned_up = True
            print(f"[Exit Cleanup] Triggering delete_files_and_create_parquet for file '{self.current_file_name}'...")
            delete_files_and_create_parquet(self.current_file_name)

    def closeEvent(self, event):
        self.cleanup()
        super().closeEvent(event)

    def process_selected_files(self, paths):
        if not paths:
            return

        file_path = paths[0]
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        self.current_file_name = file_name

        # Reset progress display
        self.welcome_page.update_progress(0, f"Starting processing for {os.path.basename(file_path)}...")

        # Spawn background processing worker thread
        self.processor_worker = VideoProcessorWorker(file_path, file_name)
        self.processor_worker.progress.connect(self.welcome_page.update_progress)
        self.processor_worker.finished.connect(lambda success, msg: self.on_processing_finished(success, msg, paths))
        self.processor_worker.start()

    def on_processing_finished(self, success, message, paths):
        if success:
            self.chat_page.set_sources(paths)
            self.pages.setCurrentWidget(self.chat_page)
        else:
            QMessageBox.critical(self, "Processing Error", f"Failed to process video:\n{message}")
            self.welcome_page.update_progress(0, "Error during processing. Please try again.")

    def process_user_query(self, query):
        if not self.current_file_name:
            self.chat_page.add_ai_message("Please select a video file first.")
            return

        self.query_worker = QueryWorker(self.current_file_name, query)
        self.query_worker.result.connect(self.on_query_result)
        self.query_worker.start()

    def on_query_result(self, query, answer):
        self.chat_page.add_ai_message(answer)

    def show_welcome_page(self):
        self.pages.setCurrentWidget(self.welcome_page)

    def toggle_theme(self):
        self.is_dark_theme = not self.is_dark_theme
        self.apply_theme(self.is_dark_theme)

    def apply_theme(self, is_dark: bool):
        self.is_dark_theme = is_dark
        theme_qss = DARK_THEME if is_dark else LIGHT_THEME
        self.setStyleSheet(theme_qss)
        self.welcome_page.update_theme_icon(is_dark)
        self.chat_page.update_theme_icon(is_dark)